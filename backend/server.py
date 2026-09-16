from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
import random
import uuid
from pathlib import Path
from pydantic import BaseModel
from typing import Optional

from stories_data import STORIES as BASE_STORIES, UNIVERSES as BASE_UNIVERSES, ERAS, STATUS_LABELS
from histoire_secrete import EXTRA_STORIES, EXTRA_UNIVERSES, DOSSIERS
from panoramas import ERA_PANORAMAS

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

EMERGENT_LLM_KEY = os.environ.get('EMERGENT_LLM_KEY')

app = FastAPI()
api_router = APIRouter(prefix="/api")

STORIES = BASE_STORIES + EXTRA_STORIES
UNIVERSES = BASE_UNIVERSES + EXTRA_UNIVERSES
STORY_INDEX = {s["id"]: s for s in STORIES}


def public_story(s: dict, full: bool = False) -> dict:
    status_key = s.get("status", "hypothese")
    out = {
        **s,
        "status_key": status_key,
        "status_meta": STATUS_LABELS.get(status_key, STATUS_LABELS["hypothese"])
    }
    if not full:
        out.pop("content", None)
        out.pop("sections", None)
        out.pop("verdict", None)
        out.pop("sources", None)
    return out


def summarize_story(s: dict) -> dict:
    """Small representation for related-links & panorama lists."""
    return {
        "id": s["id"],
        "title": s["title"],
        "subtitle": s.get("subtitle"),
        "universe": s["universe"],
        "era_label": s.get("era_label"),
        "region": s.get("region"),
        "excerpt": s.get("excerpt"),
        "status_key": s.get("status"),
        "status_meta": STATUS_LABELS.get(s.get("status", "hypothese"))
    }


@api_router.get("/")
async def root():
    return {"app": "Les Chroniques de l'Étrange", "stories": len(STORIES), "universes": len(UNIVERSES)}


@api_router.get("/universes")
async def get_universes():
    return [
        {**u, "story_count": sum(1 for s in STORIES if s["universe"] == u["id"])}
        for u in UNIVERSES
    ]


@api_router.get("/eras")
async def get_eras():
    return [
        {**e, "story_count": sum(1 for s in STORIES if s.get("era") == e["id"])}
        for e in ERAS
    ]


@api_router.get("/status-labels")
async def get_status_labels():
    return STATUS_LABELS


@api_router.get("/dossiers/{universe_id}")
async def get_dossiers(universe_id: str):
    dossiers = DOSSIERS.get(universe_id, [])
    return [
        {**d, "story_count": sum(1 for s in STORIES if s.get("universe") == universe_id and s.get("dossier") == d["id"])}
        for d in dossiers
    ]


@api_router.get("/regions")
async def get_regions():
    regions = {}
    for s in STORIES:
        r = s.get("region")
        if not r:
            continue
        regions.setdefault(r, 0)
        regions[r] += 1
    return sorted(
        [{"region": r, "story_count": c} for r, c in regions.items()],
        key=lambda x: -x["story_count"]
    )


@api_router.get("/stories")
async def list_stories(
    universe: Optional[str] = None,
    era: Optional[str] = None,
    status: Optional[str] = None,
    region: Optional[str] = None,
    dossier: Optional[str] = None,
    search: Optional[str] = None,
    limit: int = 200
):
    results = STORIES
    if universe:
        results = [s for s in results if s["universe"] == universe]
    if era:
        results = [s for s in results if s.get("era") == era]
    if status:
        results = [s for s in results if s.get("status") == status]
    if region:
        results = [s for s in results if s.get("region") == region]
    if dossier:
        results = [s for s in results if s.get("dossier") == dossier]
    if search:
        q = search.lower().strip()
        def match(s):
            hay = " ".join([
                s.get("title", ""),
                s.get("subtitle", ""),
                s.get("excerpt", ""),
                s.get("region", "") or "",
                s.get("era_label", "") or "",
                " ".join(s.get("tags", []) or []),
                " ".join(p for p in (s.get("content", []) or []) if isinstance(p, str)),
            ]).lower()
            return q in hay
        results = [s for s in results if match(s)]
    results = sorted(results, key=lambda s: s.get("year", 0))
    return [public_story(s, full=False) for s in results[:limit]]


@api_router.get("/stories/random")
async def random_story(exclude: Optional[str] = None):
    pool = [s for s in STORIES if s["id"] != exclude] if exclude else STORIES
    s = random.choice(pool)
    return public_story(s, full=True)


@api_router.get("/stories/timeline")
async def timeline():
    ordered = sorted(STORIES, key=lambda s: s.get("year", 0))
    return [
        {
            "id": s["id"],
            "title": s["title"],
            "universe": s["universe"],
            "year": s.get("year", 0),
            "era": s.get("era"),
            "era_label": s.get("era_label"),
            "region": s.get("region"),
            "status_key": s.get("status"),
            "status_meta": STATUS_LABELS.get(s.get("status", "hypothese"))
        }
        for s in ordered
    ]


@api_router.get("/stories/map")
async def map_points():
    return [
        {
            "id": s["id"],
            "title": s["title"],
            "universe": s["universe"],
            "region": s.get("region"),
            "coords": s.get("coords"),
            "excerpt": s.get("excerpt"),
            "status_key": s.get("status"),
            "status_meta": STATUS_LABELS.get(s.get("status", "hypothese"))
        }
        for s in STORIES if s.get("coords")
    ]


@api_router.get("/stories/quiz")
async def quiz_pool(limit: int = 6):
    """Try to balance the pool over multiple status categories."""
    by_status = {}
    for s in STORIES:
        by_status.setdefault(s.get("status", "hypothese"), []).append(s)
    picks = []
    keys = list(by_status.keys())
    random.shuffle(keys)
    while len(picks) < limit:
        progressed = False
        for k in keys:
            if by_status[k] and len(picks) < limit:
                picks.append(by_status[k].pop(random.randrange(len(by_status[k]))))
                progressed = True
        if not progressed:
            break
    random.shuffle(picks)
    return [
        {
            "id": s["id"],
            "title": s["title"],
            "subtitle": s.get("subtitle"),
            "excerpt": s.get("excerpt"),
            "hero_image": s.get("hero_image"),
            "status_key": s.get("status"),
            "status_meta": STATUS_LABELS.get(s.get("status", "hypothese")),
            "universe": s["universe"]
        }
        for s in picks
    ]


@api_router.get("/stories/{story_id}")
async def get_story(story_id: str):
    s = STORY_INDEX.get(story_id)
    if not s:
        raise HTTPException(404, "Récit introuvable")
    return public_story(s, full=True)


@api_router.get("/stories/{story_id}/related")
async def related_stories(story_id: str, limit: int = 4):
    s = STORY_INDEX.get(story_id)
    if not s:
        raise HTTPException(404, "Récit introuvable")
    tags = set(s.get("tags", []) or [])
    universe = s.get("universe")
    era = s.get("era")

    def score(other):
        if other["id"] == story_id:
            return -1
        sc = 0
        sc += len(tags & set(other.get("tags", []) or [])) * 3
        if other.get("universe") == universe:
            sc += 2
        if other.get("era") == era:
            sc += 1
        return sc

    ranked = sorted(STORIES, key=score, reverse=True)
    picks = [x for x in ranked if x["id"] != story_id and score(x) > 0][:limit]
    return [summarize_story(x) for x in picks]


# ============ VOYAGE DANS LE TEMPS ============
@api_router.get("/panoramas")
async def get_panoramas():
    return [
        {
            "id": p["id"],
            "label": p["label"],
            "period": p["period"],
            "tagline": p["tagline"],
            "hero_image": p["hero_image"],
            "story_count": len(p.get("linked_story_ids", []))
        }
        for p in ERA_PANORAMAS.values()
    ]


@api_router.get("/panoramas/{era_id}")
async def get_panorama(era_id: str):
    p = ERA_PANORAMAS.get(era_id)
    if not p:
        raise HTTPException(404, "Époque introuvable")
    linked = [summarize_story(STORY_INDEX[i]) for i in p.get("linked_story_ids", []) if i in STORY_INDEX]
    return {**p, "linked_stories": linked}


# ============ AI ============
class GenerateRequest(BaseModel):
    prompt: str
    universe: Optional[str] = None


@api_router.post("/ai/tell-strange")
async def tell_strange_ai(req: GenerateRequest):
    if not EMERGENT_LLM_KEY:
        raise HTTPException(500, "LLM key non configurée")

    from emergentintegrations.llm.chat import LlmChat, UserMessage, TextDelta, StreamDone

    system = (
        "Tu es le narrateur des « Chroniques de l'Étrange », une application francophone consacrée "
        "à l'histoire du mysticisme, de l'occultisme, de l'ésotérisme, des arts divinatoires et des légendes. "
        "TON : passionné, oral, vulgarisateur, sans jargon. Aucune emphase mystique gratuite. "
        "RÈGLE ABSOLUE : commence toujours par étiqueter clairement le statut de ce que tu vas raconter — "
        "« Fait historique attesté », « Tradition ou croyance », « Conte ou légende » ou « Hypothèse ». "
        "N'invente jamais de sources précises. Longueur : 4 à 6 paragraphes, ~300 mots. "
        "Termine par « Pour aller plus loin : » avec des pistes générales (auteurs, musées)."
    )

    chat = LlmChat(
        api_key=EMERGENT_LLM_KEY,
        session_id=f"strange-{uuid.uuid4()}",
        system_message=system
    ).with_model("anthropic", "claude-sonnet-5")

    user_prompt = req.prompt or "Raconte-moi une anecdote historique étrange et véridique."

    async def event_generator():
        try:
            async for ev in chat.stream_message(UserMessage(text=user_prompt)):
                if isinstance(ev, TextDelta):
                    yield f"data: {ev.content}\n\n"
                elif isinstance(ev, StreamDone):
                    yield "data: [DONE]\n\n"
                    break
        except Exception as e:
            logging.exception("LLM streaming failed")
            yield f"data: [ERROR] {str(e)}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"}
    )


app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()

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
from typing import Optional, List

from stories_data import STORIES, UNIVERSES, ERAS, STATUS_LABELS

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

EMERGENT_LLM_KEY = os.environ.get('EMERGENT_LLM_KEY')

app = FastAPI()
api_router = APIRouter(prefix="/api")

# Index by id
STORY_INDEX = {s["id"]: s for s in STORIES}


def public_story(s: dict, full: bool = False) -> dict:
    """Return a story with status metadata."""
    status_key = s.get("status", "hypothese")
    out = {
        **s,
        "status_key": status_key,
        "status_meta": STATUS_LABELS.get(status_key, STATUS_LABELS["hypothese"])
    }
    if not full:
        out.pop("content", None)
        out.pop("sources", None)
    return out


@api_router.get("/")
async def root():
    return {"app": "Les Chroniques de l'Étrange", "stories": len(STORIES)}


@api_router.get("/universes")
async def get_universes():
    # Attach counts
    out = []
    for u in UNIVERSES:
        count = sum(1 for s in STORIES if s["universe"] == u["id"])
        out.append({**u, "story_count": count})
    return out


@api_router.get("/eras")
async def get_eras():
    out = []
    for e in ERAS:
        count = sum(1 for s in STORIES if s.get("era") == e["id"])
        out.append({**e, "story_count": count})
    return out


@api_router.get("/status-labels")
async def get_status_labels():
    return STATUS_LABELS


@api_router.get("/stories")
async def list_stories(
    universe: Optional[str] = None,
    era: Optional[str] = None,
    status: Optional[str] = None,
    search: Optional[str] = None,
    limit: int = 100
):
    results = STORIES
    if universe:
        results = [s for s in results if s["universe"] == universe]
    if era:
        results = [s for s in results if s.get("era") == era]
    if status:
        results = [s for s in results if s.get("status") == status]
    if search:
        q = search.lower()
        results = [
            s for s in results
            if q in s["title"].lower()
            or q in s.get("subtitle", "").lower()
            or q in s.get("excerpt", "").lower()
            or any(q in t for t in s.get("tags", []))
        ]
    results = sorted(results, key=lambda s: s.get("year", 0))
    return [public_story(s, full=False) for s in results[:limit]]


@api_router.get("/stories/random")
async def random_story():
    s = random.choice(STORIES)
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
async def quiz_pool(limit: int = 5):
    """Return a randomized list of stories for the 'Vrai, croyance ou légende ?' quiz."""
    pool = random.sample(STORIES, k=min(limit, len(STORIES)))
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
        for s in pool
    ]


@api_router.get("/stories/{story_id}")
async def get_story(story_id: str):
    s = STORY_INDEX.get(story_id)
    if not s:
        raise HTTPException(404, "Récit introuvable")
    return public_story(s, full=True)


# ============ AI: Génération de récit à la demande ============
class GenerateRequest(BaseModel):
    prompt: str
    universe: Optional[str] = None


@api_router.post("/ai/tell-strange")
async def tell_strange_ai(req: GenerateRequest):
    """Generate a short, original 'strange but true' historical anecdote via Claude Sonnet 5.
    Streams as SSE. Always uses the sober editorial rules of the app.
    """
    if not EMERGENT_LLM_KEY:
        raise HTTPException(500, "LLM key non configurée")

    from emergentintegrations.llm.chat import LlmChat, UserMessage, TextDelta, StreamDone

    system = (
        "Tu es le narrateur des « Chroniques de l'Étrange », une application francophone consacrée "
        "à l'histoire du mysticisme, de l'occultisme, de l'ésotérisme, des arts divinatoires et des légendes. "
        "TON : passionné, oral, vulgarisateur, sans jargon. Aucune emphase mystique gratuite. "
        "RÈGLE ABSOLUE : commence toujours par étiqueter clairement le statut de ce que tu vas raconter — "
        "« Fait historique attesté », « Tradition ou croyance », « Conte ou légende » ou « Hypothèse ». "
        "N'invente jamais de sources précises. Ne présente pas une légende comme un fait. "
        "Longueur : 4 à 6 paragraphes, environ 300 mots. "
        "Termine par une ligne « Pour aller plus loin : » avec des pistes de lecture générales (auteurs, musées) "
        "sans inventer de références précises."
    )

    chat = LlmChat(
        api_key=EMERGENT_LLM_KEY,
        session_id=f"strange-{uuid.uuid4()}",
        system_message=system
    ).with_model("anthropic", "claude-sonnet-5")

    user_prompt = req.prompt or "Raconte-moi une anecdote historique étrange et véridique, en indiquant clairement son statut."

    async def event_generator():
        try:
            async for ev in chat.stream_message(UserMessage(text=user_prompt)):
                if isinstance(ev, TextDelta):
                    # SSE: prefix each chunk
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

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()

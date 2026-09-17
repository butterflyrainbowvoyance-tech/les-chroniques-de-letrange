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
from origines import ORIGINES
from morts_etranges import MORTS_UNIVERSE, MORTS_STORIES
from lieux_hantes import LIEUX_UNIVERSE, LIEUX_STORIES, LIEUX_DOSSIERS

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

EMERGENT_LLM_KEY = os.environ.get('EMERGENT_LLM_KEY')
ADMIN_TOKEN = os.environ.get('ADMIN_TOKEN', 'change-me')

app = FastAPI()
api_router = APIRouter(prefix="/api")

STORIES = BASE_STORIES + EXTRA_STORIES + MORTS_STORIES + LIEUX_STORIES
UNIVERSES = BASE_UNIVERSES + EXTRA_UNIVERSES + [MORTS_UNIVERSE, LIEUX_UNIVERSE]
# Merge dossiers per universe
DOSSIERS = {**DOSSIERS, "lieux-hantes": LIEUX_DOSSIERS}
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
        out.pop("specs", None)
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


# ============ À L'ORIGINE DE… ============
@api_router.get("/origines")
async def list_origines():
    return [
        {
            "id": o["id"],
            "symbol": o["symbol"],
            "hook": o["hook"],
            "one_liner": o["one_liner"],
            "hero_image": o["hero_image"],
            "tags": o.get("tags", [])
        }
        for o in ORIGINES
    ]


@api_router.get("/origines/{origine_id}")
async def get_origine(origine_id: str):
    for o in ORIGINES:
        if o["id"] == origine_id:
            return o
    raise HTTPException(404, "Origine introuvable")


# ============ LIVRE DU SOIR ============
from datetime import datetime, timezone, timedelta
try:
    from zoneinfo import ZoneInfo
    PARIS_TZ = ZoneInfo("Europe/Paris")
except Exception:
    PARIS_TZ = timezone.utc

def _paris_today():
    return datetime.now(PARIS_TZ).date()

def _pick_for_date(d: datetime) -> dict:
    """Deterministic pick based on ordinal day."""
    ordered = sorted(STORIES, key=lambda s: s["id"])
    idx = d.toordinal() % len(ordered)
    return ordered[idx]


@api_router.get("/livre-du-soir")
async def livre_du_soir():
    today = _paris_today()
    s = _pick_for_date(datetime.fromordinal(today.toordinal()))
    return {
        "date": today.isoformat(),
        "greeting": _greeting_for(today),
        "story": public_story(s, full=True)
    }


@api_router.get("/livre-du-soir/history")
async def livre_du_soir_history(days: int = 7):
    today = _paris_today()
    out = []
    for i in range(days):
        d = today - timedelta(days=i)
        s = _pick_for_date(datetime.fromordinal(d.toordinal()))
        out.append({"date": d.isoformat(), "story": summarize_story(s)})
    return out


_GREETINGS = [
    "Ce soir, on ouvre…",
    "La chronique de la nuit :",
    "Une histoire pour votre veillée :",
    "Ce que la bibliothèque vous propose ce soir :",
    "L'entrée du soir dans nos archives :",
    "Une lecture pour la nuit qui vient :",
    "La page qu'on tourne ensemble ce soir :",
]

def _greeting_for(d) -> str:
    return _GREETINGS[d.toordinal() % len(_GREETINGS)]


# ============ AUDIO NARRATION (OpenAI TTS) ============
import re
import hashlib
from fastapi import Response

AUDIO_CACHE_DIR = ROOT_DIR / "tts_cache"
AUDIO_CACHE_DIR.mkdir(exist_ok=True)


def _sanitize_for_tts(text: str) -> str:
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"`{1,3}[^`]*`{1,3}", "", text)
    text = re.sub(r"[*_#>~|]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _story_narration_text(s: dict) -> str:
    parts = [s.get("title", "")]
    if s.get("subtitle"):
        parts.append(s["subtitle"] + ".")
    if s.get("excerpt"):
        parts.append(s["excerpt"])
    if s.get("content"):
        parts.extend(s["content"])
    elif s.get("sections"):
        for sec in s["sections"]:
            parts.append(sec.get("title", "") + ".")
            parts.extend(sec.get("paragraphs", []))
    text = _sanitize_for_tts(" ".join(parts))
    # OpenAI TTS 4096 chars per request; take an evocative excerpt
    return text[:3800]


@api_router.get("/audio/story/{story_id}.mp3")
async def narrate_story(story_id: str):
    s = STORY_INDEX.get(story_id)
    if not s:
        raise HTTPException(404, "Récit introuvable")
    if not EMERGENT_LLM_KEY:
        raise HTTPException(500, "Clé LLM absente")

    text = _story_narration_text(s)
    voice = "nova"
    model = "tts-1-hd"
    key = hashlib.sha256(f"{story_id}|{voice}|{model}|{text}".encode()).hexdigest()[:24]
    cache_path = AUDIO_CACHE_DIR / f"{key}.mp3"

    if not cache_path.exists():
        from emergentintegrations.llm.openai import OpenAITextToSpeech
        tts = OpenAITextToSpeech(api_key=EMERGENT_LLM_KEY)
        try:
            audio = await tts.generate_speech(
                text=text, model=model, voice=voice, response_format="mp3", speed=0.95
            )
        except Exception as e:
            logging.exception("TTS generation failed")
            raise HTTPException(502, f"Génération audio impossible: {e}")
        cache_path.write_bytes(audio)

    return Response(
        content=cache_path.read_bytes(),
        media_type="audio/mpeg",
        headers={"Cache-Control": "public, max-age=31536000"}
    )


# ============ ADMIN + USER CONTENT ============
from fastapi import Header, Depends
import uuid as _uuid
from datetime import datetime as _dt

async def require_admin(authorization: Optional[str] = Header(None)):
    token = (authorization or "").replace("Bearer ", "").strip()
    if not token or token != ADMIN_TOKEN:
        raise HTTPException(401, "Accès administrateur refusé")
    return True


def _clean_story_doc(doc: dict) -> dict:
    doc.pop("_id", None)
    doc["is_user_content"] = True
    return doc


async def _reload_user_content():
    """Rebuild the global STORIES + STORY_INDEX with base + Mongo user stories."""
    global STORIES, STORY_INDEX
    # Keep only non-user-content
    base = [s for s in STORIES if not s.get("is_user_content")]
    user_docs = await db.user_stories.find().to_list(1000)
    user_stories = [_clean_story_doc(d) for d in user_docs]
    STORIES.clear()
    STORIES.extend(base + user_stories)
    STORY_INDEX.clear()
    STORY_INDEX.update({s["id"]: s for s in STORIES})


@app.on_event("startup")
async def _on_startup():
    try:
        await _reload_user_content()
    except Exception:
        logging.exception("Failed to reload user content on startup")


class AdminStoryIn(BaseModel):
    universe: str
    dossier: Optional[str] = None
    title: str
    subtitle: Optional[str] = ""
    status: str = "hypothese"
    era: Optional[str] = None
    era_label: Optional[str] = ""
    year: int = 0
    region: Optional[str] = ""
    coords: Optional[list] = None
    hero_image: Optional[str] = ""
    excerpt: str
    content: list  # list of paragraphs
    sources: Optional[list] = []
    tags: Optional[list] = []


@api_router.get("/admin/check")
async def admin_check(_: bool = Depends(require_admin)):
    return {"ok": True}


@api_router.get("/admin/stories")
async def admin_list_stories(_: bool = Depends(require_admin)):
    docs = await db.user_stories.find().to_list(1000)
    return [_clean_story_doc(d) for d in docs]


@api_router.post("/admin/stories")
async def admin_create_story(payload: AdminStoryIn, _: bool = Depends(require_admin)):
    slug = "".join(c if c.isalnum() else "-" for c in payload.title.lower())[:60].strip("-")
    doc = payload.model_dump()
    doc["id"] = f"user-{slug}-{_uuid.uuid4().hex[:6]}"
    doc["created_at"] = _dt.now(timezone.utc).isoformat()
    doc["is_user_content"] = True
    await db.user_stories.insert_one(doc.copy())
    await _reload_user_content()
    return public_story(STORY_INDEX[doc["id"]], full=True)


@api_router.patch("/admin/stories/{story_id}")
async def admin_edit_story(story_id: str, payload: AdminStoryIn, _: bool = Depends(require_admin)):
    update = payload.model_dump(exclude_unset=True)
    update["updated_at"] = _dt.now(timezone.utc).isoformat()
    res = await db.user_stories.update_one({"id": story_id}, {"$set": update})
    if res.matched_count == 0:
        raise HTTPException(404, "Chronique introuvable (ou récit de base non modifiable)")
    await _reload_user_content()
    return public_story(STORY_INDEX[story_id], full=True)


@api_router.delete("/admin/stories/{story_id}")
async def admin_delete_story(story_id: str, _: bool = Depends(require_admin)):
    res = await db.user_stories.delete_one({"id": story_id})
    await _reload_user_content()
    return {"deleted": res.deleted_count}


# ============ AVIS (reviews) ============
class ReviewIn(BaseModel):
    name: str
    rating: int  # 1..5
    comment: str


@api_router.get("/reviews")
async def list_reviews(limit: int = 50):
    docs = await db.reviews.find({"published": {"$ne": False}}).sort("created_at", -1).to_list(limit)
    for d in docs:
        d.pop("_id", None)
    return docs


@api_router.post("/reviews")
async def create_review(payload: ReviewIn):
    if payload.rating < 1 or payload.rating > 5:
        raise HTTPException(400, "Note doit être entre 1 et 5")
    if not payload.name.strip() or not payload.comment.strip():
        raise HTTPException(400, "Nom et commentaire requis")
    doc = {
        "id": _uuid.uuid4().hex[:12],
        "name": payload.name.strip()[:60],
        "rating": payload.rating,
        "comment": payload.comment.strip()[:1500],
        "created_at": _dt.now(timezone.utc).isoformat(),
        "published": False,
        "status": "pending"
    }
    await db.reviews.insert_one(doc.copy())
    doc.pop("_id", None)
    return {"received": True, "message": "Merci — votre avis sera lu par la rédaction avant publication."}


class ReviewModerateIn(BaseModel):
    action: str  # approve | refuse
    name: Optional[str] = None
    rating: Optional[int] = None
    comment: Optional[str] = None


@api_router.get("/admin/reviews")
async def admin_list_reviews(_: bool = Depends(require_admin)):
    docs = await db.reviews.find().sort("created_at", -1).to_list(1000)
    for d in docs:
        d.pop("_id", None)
    return docs


@api_router.patch("/admin/reviews/{review_id}")
async def admin_moderate_review(review_id: str, payload: ReviewModerateIn, _: bool = Depends(require_admin)):
    update = {}
    if payload.name is not None: update["name"] = payload.name.strip()[:60]
    if payload.rating is not None: update["rating"] = max(1, min(5, payload.rating))
    if payload.comment is not None: update["comment"] = payload.comment.strip()[:1500]
    if payload.action == "approve":
        update["published"] = True
        update["status"] = "approved"
    elif payload.action == "refuse":
        update["published"] = False
        update["status"] = "refused"
    if not update:
        raise HTTPException(400, "Aucune modification")
    await db.reviews.update_one({"id": review_id}, {"$set": update})
    return {"ok": True}


@api_router.delete("/admin/reviews/{review_id}")
async def admin_delete_review(review_id: str, _: bool = Depends(require_admin)):
    res = await db.reviews.delete_one({"id": review_id})
    return {"deleted": res.deleted_count}


@api_router.get("/reviews/summary")
async def reviews_summary():
    docs = await db.reviews.find({"published": {"$ne": False}}).to_list(10000)
    if not docs:
        return {"count": 0, "average": 0}
    avg = sum(d["rating"] for d in docs) / len(docs)
    return {"count": len(docs), "average": round(avg, 2)}


# ============ TÉMOIGNAGES ============
class TestimonyIn(BaseModel):
    name: str
    location: Optional[str] = ""
    title: str
    story: str


@api_router.get("/temoignages")
async def list_temoignages(limit: int = 50):
    docs = await db.temoignages.find({"published": {"$ne": False}}).sort("created_at", -1).to_list(limit)
    for d in docs:
        d.pop("_id", None)
    return docs


@api_router.post("/temoignages")
async def create_temoignage(payload: TestimonyIn):
    if not payload.name.strip() or not payload.title.strip() or not payload.story.strip():
        raise HTTPException(400, "Nom, titre et récit requis")
    doc = {
        "id": _uuid.uuid4().hex[:12],
        "name": payload.name.strip()[:60],
        "location": (payload.location or "").strip()[:120],
        "title": payload.title.strip()[:120],
        "story": payload.story.strip()[:5000],
        "created_at": _dt.now(timezone.utc).isoformat(),
        "published": False,
        "status": "pending"
    }
    await db.temoignages.insert_one(doc.copy())
    doc.pop("_id", None)
    return {"received": True, "message": "Merci — votre témoignage sera lu par la rédaction avant publication."}


class TemoignageModerateIn(BaseModel):
    action: str
    name: Optional[str] = None
    location: Optional[str] = None
    title: Optional[str] = None
    story: Optional[str] = None


@api_router.get("/admin/temoignages")
async def admin_list_temoignages(_: bool = Depends(require_admin)):
    docs = await db.temoignages.find().sort("created_at", -1).to_list(1000)
    for d in docs:
        d.pop("_id", None)
    return docs


@api_router.patch("/admin/temoignages/{temoignage_id}")
async def admin_moderate_temoignage(temoignage_id: str, payload: TemoignageModerateIn, _: bool = Depends(require_admin)):
    update = {}
    for f in ("name", "location", "title", "story"):
        v = getattr(payload, f)
        if v is not None: update[f] = v.strip()
    if payload.action == "approve":
        update["published"] = True
        update["status"] = "approved"
    elif payload.action == "refuse":
        update["published"] = False
        update["status"] = "refused"
    if not update:
        raise HTTPException(400, "Aucune modification")
    await db.temoignages.update_one({"id": temoignage_id}, {"$set": update})
    return {"ok": True}


@api_router.delete("/admin/temoignages/{temoignage_id}")
async def admin_delete_temoignage(temoignage_id: str, _: bool = Depends(require_admin)):
    res = await db.temoignages.delete_one({"id": temoignage_id})
    return {"deleted": res.deleted_count}


# ============ COLLABORATIONS & ENQUÊTES ============
class CollaborationIn(BaseModel):
    name: str
    email: str
    kind: str  # podcast, video, interview, conference, enquete, visite, recherche, contenu, autre
    project: str
    links: Optional[str] = ""
    message: str


class EnqueteIn(BaseModel):
    name: str
    email: str
    role: Optional[str] = ""  # propriétaire, association, particulier…
    place_name: str
    place_location: str
    tradition_summary: str
    message: Optional[str] = ""


@api_router.post("/collaborations")
async def create_collab(payload: CollaborationIn):
    if not payload.name.strip() or not payload.email.strip() or not payload.project.strip() or not payload.message.strip():
        raise HTTPException(400, "Champs obligatoires manquants")
    doc = {
        "id": _uuid.uuid4().hex[:12],
        **{k: (getattr(payload, k) or "").strip() for k in ["name","email","kind","project","links","message"]},
        "created_at": _dt.now(timezone.utc).isoformat(),
        "status": "pending",
        "published": False
    }
    await db.collaborations.insert_one(doc.copy())
    return {"received": True, "message": "Merci — votre proposition arrive dans notre espace de rédaction."}


@api_router.post("/enquetes")
async def create_enquete(payload: EnqueteIn):
    if not payload.name.strip() or not payload.email.strip() or not payload.place_name.strip() or not payload.tradition_summary.strip():
        raise HTTPException(400, "Champs obligatoires manquants")
    doc = {
        "id": _uuid.uuid4().hex[:12],
        **{k: (getattr(payload, k) or "").strip() for k in ["name","email","role","place_name","place_location","tradition_summary","message"]},
        "created_at": _dt.now(timezone.utc).isoformat(),
        "status": "pending",
        "published": False
    }
    await db.enquetes.insert_one(doc.copy())
    return {"received": True, "message": "Merci — votre proposition arrive dans notre espace de rédaction."}


@api_router.get("/admin/collaborations")
async def admin_list_collabs(_: bool = Depends(require_admin)):
    docs = await db.collaborations.find().sort("created_at", -1).to_list(1000)
    for d in docs: d.pop("_id", None)
    return docs


@api_router.patch("/admin/collaborations/{cid}")
async def admin_mod_collab(cid: str, payload: dict, _: bool = Depends(require_admin)):
    update = {}
    action = payload.get("action")
    if action == "approve": update["status"] = "approved"
    elif action == "refuse": update["status"] = "refused"
    elif action == "processed": update["status"] = "processed"
    for k in ["name","email","kind","project","links","message"]:
        if k in payload and payload[k] is not None: update[k] = str(payload[k]).strip()
    await db.collaborations.update_one({"id": cid}, {"$set": update})
    return {"ok": True}


@api_router.delete("/admin/collaborations/{cid}")
async def admin_del_collab(cid: str, _: bool = Depends(require_admin)):
    await db.collaborations.delete_one({"id": cid})
    return {"ok": True}


@api_router.get("/admin/enquetes")
async def admin_list_enquetes(_: bool = Depends(require_admin)):
    docs = await db.enquetes.find().sort("created_at", -1).to_list(1000)
    for d in docs: d.pop("_id", None)
    return docs


@api_router.patch("/admin/enquetes/{eid}")
async def admin_mod_enquete(eid: str, payload: dict, _: bool = Depends(require_admin)):
    update = {}
    action = payload.get("action")
    if action == "approve": update["status"] = "approved"
    elif action == "refuse": update["status"] = "refused"
    elif action == "processed": update["status"] = "processed"
    for k in ["name","email","role","place_name","place_location","tradition_summary","message"]:
        if k in payload and payload[k] is not None: update[k] = str(payload[k]).strip()
    await db.enquetes.update_one({"id": eid}, {"$set": update})
    return {"ok": True}


@api_router.delete("/admin/enquetes/{eid}")
async def admin_del_enquete(eid: str, _: bool = Depends(require_admin)):
    await db.enquetes.delete_one({"id": eid})
    return {"ok": True}


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

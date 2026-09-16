"""Backend API tests for Les Chroniques de l'Étrange (iteration 2)."""
import os
import requests
import pytest
from dotenv import load_dotenv

load_dotenv('/app/frontend/.env')
BASE_URL = os.environ["REACT_APP_BACKEND_URL"].rstrip("/")
API = f"{BASE_URL}/api"


# ---------- Root / catalog ----------
def test_root_counts():
    r = requests.get(f"{API}/")
    assert r.status_code == 200
    data = r.json()
    assert data.get("stories") == 45, f"expected 45 stories, got {data.get('stories')}"
    assert data.get("universes") == 10, f"expected 10 universes, got {data.get('universes')}"


def test_universes_10_and_keys():
    r = requests.get(f"{API}/universes")
    assert r.status_code == 200
    data = r.json()
    ids = [u["id"] for u in data]
    assert len(data) == 10, f"expected 10 universes, got {len(data)}: {ids}"
    for req in ["histoire-secrete", "ils-y-croyaient", "legende-vs-archives"]:
        assert req in ids, f"missing universe {req}"
    for u in data:
        assert "story_count" in u


def test_eras_present():
    r = requests.get(f"{API}/eras")
    assert r.status_code == 200
    assert len(r.json()) >= 5


# ---------- Dossiers / Regions ----------
def test_dossiers_histoire_secrete():
    r = requests.get(f"{API}/dossiers/histoire-secrete")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list) and len(data) > 0
    for d in data:
        assert "id" in d and "story_count" in d


def test_regions_has_counts():
    r = requests.get(f"{API}/regions")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list) and len(data) > 0
    for row in data:
        assert "region" in row and "story_count" in row and row["story_count"] > 0


# ---------- Panoramas ----------
def test_panoramas_list_five_eras():
    r = requests.get(f"{API}/panoramas")
    assert r.status_code == 200
    data = r.json()
    ids = [p["id"] for p in data]
    for req in ["antiquite", "moyen-age", "renaissance", "moderne", "xixe"]:
        assert req in ids, f"missing panorama {req}. got {ids}"
    assert len(data) == 5


def test_panorama_renaissance_full():
    r = requests.get(f"{API}/panoramas/renaissance")
    assert r.status_code == 200
    data = r.json()
    for k in ["belief", "practice", "consult", "objects", "fear"]:
        assert k in data, f"missing key {k} in panorama"
        assert isinstance(data[k], list) and len(data[k]) > 0
    assert "linked_stories" in data and isinstance(data["linked_stories"], list)


def test_panorama_unknown_404():
    r = requests.get(f"{API}/panoramas/does-not-exist")
    assert r.status_code == 404


# ---------- Search / filter ----------
def test_search_raspoutine():
    r = requests.get(f"{API}/stories", params={"search": "Raspoutine"})
    assert r.status_code == 200
    ids = [s["id"] for s in r.json()]
    assert "raspoutine-romanov" in ids
    assert "archives-raspoutine" in ids
    assert len(ids) >= 2


def test_search_tarot():
    r = requests.get(f"{API}/stories", params={"search": "tarot"})
    assert r.status_code == 200
    ids = [s["id"] for s in r.json()]
    assert "tarot-histoire" in ids


def test_filter_region_paris():
    r = requests.get(f"{API}/stories", params={"region": "Paris"})
    assert r.status_code == 200
    data = r.json()
    assert len(data) > 0
    assert all(s.get("region") == "Paris" for s in data)


# ---------- Story detail with sections/verdict ----------
def test_archives_flamel_sections_and_verdict():
    r = requests.get(f"{API}/stories/archives-flamel")
    assert r.status_code == 200
    data = r.json()
    assert data.get("format") == "legende-vs-archives"
    sections = data.get("sections") or []
    assert len(sections) == 2, f"expected 2 sections got {len(sections)}"
    verdict = data.get("verdict")
    assert isinstance(verdict, list) and len(verdict) > 0
    assert isinstance(data.get("sources"), list) and len(data["sources"]) > 0
    assert isinstance(data.get("tags"), list) and len(data["tags"]) > 0


def test_ils_astrologue_du_roi_sections():
    r = requests.get(f"{API}/stories/ils-astrologue-du-roi")
    assert r.status_code == 200
    data = r.json()
    assert data.get("format") == "ils-y-croyaient"
    sections = data.get("sections") or []
    assert len(sections) == 4, f"expected 4 sections got {len(sections)}"


# ---------- Related ----------
def test_related_nostradamus():
    r = requests.get(f"{API}/stories/nostradamus/related")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list) and len(data) > 0
    assert all(x["id"] != "nostradamus" for x in data)
    for x in data:
        assert "title" in x and "universe" in x


# ---------- Random exclude ----------
def test_random_exclude_nostradamus():
    for _ in range(15):
        r = requests.get(f"{API}/stories/random", params={"exclude": "nostradamus"})
        assert r.status_code == 200
        assert r.json()["id"] != "nostradamus"


# ---------- Quiz ----------
def test_quiz_balanced_pool():
    r = requests.get(f"{API}/stories/quiz", params={"limit": 6})
    assert r.status_code == 200
    data = r.json()
    assert len(data) == 6
    statuses = {d["status_key"] for d in data}
    assert len(statuses) >= 2, "expected at least 2 different status keys in a 6-quiz pool"


# ---------- Not-found guard ----------
def test_story_not_found():
    r = requests.get(f"{API}/stories/does-not-exist-xyz")
    assert r.status_code == 404



# ---------- Origines (À l'origine de…) ----------
def test_origines_list_six():
    r = requests.get(f"{API}/origines")
    assert r.status_code == 200
    data = r.json()
    assert len(data) == 6, f"expected 6 origines, got {len(data)}"
    required = {"id", "symbol", "hook", "one_liner", "hero_image", "tags"}
    for o in data:
        assert required.issubset(o.keys()), f"missing keys in {o.get('id')}: have {o.keys()}"
        assert isinstance(o["tags"], list)


def test_origine_sel_renverse_full():
    r = requests.get(f"{API}/origines/sel-renverse")
    assert r.status_code == 200
    data = r.json()
    sections = data.get("sections") or []
    assert len(sections) == 4, f"expected 4 sections got {len(sections)}"
    for sec in sections:
        assert sec.get("title")
        assert isinstance(sec.get("paragraphs"), list) and len(sec["paragraphs"]) > 0
    sources = data.get("sources") or []
    assert len(sources) == 3, f"expected 3 sources got {len(sources)}"
    assert isinstance(data.get("tags"), list) and len(data["tags"]) > 0


def test_origine_unknown_404():
    r = requests.get(f"{API}/origines/does-not-exist")
    assert r.status_code == 404

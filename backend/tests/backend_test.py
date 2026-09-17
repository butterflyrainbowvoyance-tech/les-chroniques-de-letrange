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
    assert data.get("stories") == 62, f"expected 62 stories, got {data.get('stories')}"
    assert data.get("universes") == 12, f"expected 12 universes, got {data.get('universes')}"


def test_universes_10_and_keys():
    r = requests.get(f"{API}/universes")
    assert r.status_code == 200
    data = r.json()
    ids = [u["id"] for u in data]
    assert len(data) == 12, f"expected 12 universes, got {len(data)}: {ids}"
    for req in ["histoire-secrete", "ils-y-croyaient", "legende-vs-archives", "morts-etranges"]:
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


# ---------- Livre du soir ----------
def test_livre_du_soir_today():
    r = requests.get(f"{API}/livre-du-soir")
    assert r.status_code == 200
    data = r.json()
    assert "date" in data and "greeting" in data and "story" in data
    assert isinstance(data["greeting"], str) and len(data["greeting"]) > 0
    s = data["story"]
    assert "id" in s and "title" in s and "status_key" in s
    # full: has content or sections + sources typical
    assert ("content" in s) or ("sections" in s)


def test_livre_du_soir_deterministic():
    r1 = requests.get(f"{API}/livre-du-soir").json()
    r2 = requests.get(f"{API}/livre-du-soir").json()
    assert r1["story"]["id"] == r2["story"]["id"]
    assert r1["date"] == r2["date"]
    assert r1["greeting"] == r2["greeting"]


def test_livre_du_soir_history_7():
    r = requests.get(f"{API}/livre-du-soir/history", params={"days": 7})
    assert r.status_code == 200
    data = r.json()
    assert len(data) == 7
    dates = [e["date"] for e in data]
    assert dates == sorted(dates, reverse=True)
    today_r = requests.get(f"{API}/livre-du-soir").json()
    assert data[0]["date"] == today_r["date"]
    assert data[0]["story"]["id"] == today_r["story"]["id"]
    for e in data:
        assert "id" in e["story"] and "title" in e["story"]



# ---------- Morts étranges (new universe) ----------
def test_universe_morts_etranges_count_8():
    r = requests.get(f"{API}/universes")
    assert r.status_code == 200
    me = next((u for u in r.json() if u["id"] == "morts-etranges"), None)
    assert me is not None, "morts-etranges universe missing"
    assert me.get("story_count") == 8, f"expected 8 stories, got {me.get('story_count')}"


def test_morts_etranges_stories_list():
    r = requests.get(f"{API}/stories", params={"universe": "morts-etranges"})
    assert r.status_code == 200
    data = r.json()
    ids = {s["id"] for s in data}
    expected = {
        "mort-mozart", "mort-hendrick-jeanne-albret", "mort-poe",
        "mort-cesare-borgia", "mort-tycho-brahe", "mort-crowley",
        "mort-jeanne-arc", "mort-alexandre-le-grand",
    }
    assert expected.issubset(ids), f"missing ids: {expected - ids}"
    assert len(data) == 8


def test_mort_mozart_detail():
    r = requests.get(f"{API}/stories/mort-mozart")
    assert r.status_code == 200
    data = r.json()
    assert data.get("id") == "mort-mozart"
    assert (data.get("content") or data.get("sections"))
    assert isinstance(data.get("sources"), list) and len(data["sources"]) > 0
    assert isinstance(data.get("tags"), list) and len(data["tags"]) > 0


# ---------- TTS audio endpoint ----------
def test_audio_story_mort_mozart_generates_and_caches():
    url = f"{API}/audio/story/mort-mozart.mp3"
    r1 = requests.get(url, timeout=60)
    assert r1.status_code == 200, f"got {r1.status_code}: {r1.text[:200]}"
    ct = r1.headers.get("Content-Type", "")
    assert "audio/mpeg" in ct, f"unexpected content-type: {ct}"
    assert len(r1.content) > 100_000, f"body too small: {len(r1.content)}"

    # Second call should be served from cache (fast)
    r2 = requests.get(url, timeout=15)
    assert r2.status_code == 200
    assert "audio/mpeg" in r2.headers.get("Content-Type", "")
    assert len(r2.content) > 100_000


def test_audio_story_unknown_404():
    r = requests.get(f"{API}/audio/story/unknown-id-xyz.mp3")
    assert r.status_code == 404



# ---------- Lieux hantés (iteration 6) ----------
def test_universe_lieux_hantes_count_9():
    r = requests.get(f"{API}/universes")
    assert r.status_code == 200
    lh = next((u for u in r.json() if u["id"] == "lieux-hantes"), None)
    assert lh is not None, "lieux-hantes universe missing"
    assert lh.get("story_count") == 9, f"expected 9, got {lh.get('story_count')}"


def test_lieux_hantes_stories_list():
    r = requests.get(f"{API}/stories", params={"universe": "lieux-hantes"})
    assert r.status_code == 200
    data = r.json()
    ids = {s["id"] for s in data}
    expected = {"lieu-brissac", "lieu-mortemer", "lieu-broceliande", "lieu-pere-lachaise",
                "lieu-combourg", "lieu-tour-londres", "lieu-glamis", "lieu-poveglia", "lieu-aokigahara"}
    assert expected.issubset(ids), f"missing: {expected - ids}"
    assert len(data) == 9


def test_lieux_hantes_dossier_france():
    r = requests.get(f"{API}/stories", params={"universe": "lieux-hantes", "dossier": "france"})
    assert r.status_code == 200
    data = r.json()
    assert len(data) == 5, f"expected 5 france, got {len(data)}"
    assert all(s.get("dossier") == "france" for s in data)


def test_lieux_hantes_dossier_monde():
    r = requests.get(f"{API}/stories", params={"universe": "lieux-hantes", "dossier": "monde"})
    assert r.status_code == 200
    data = r.json()
    assert len(data) == 4, f"expected 4 monde, got {len(data)}"
    assert all(s.get("dossier") == "monde" for s in data)


def test_dossiers_lieux_hantes():
    r = requests.get(f"{API}/dossiers/lieux-hantes")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list) and len(data) == 2
    by_id = {d["id"]: d for d in data}
    assert "france" in by_id and "monde" in by_id
    assert by_id["france"]["story_count"] == 5
    assert by_id["monde"]["story_count"] == 4


def test_lieu_brissac_detail():
    r = requests.get(f"{API}/stories/lieu-brissac")
    assert r.status_code == 200
    data = r.json()
    specs = data.get("specs")
    assert isinstance(specs, list) and len(specs) == 5
    for row in specs:
        assert "label" in row and "value" in row
    assert data.get("place_type")
    assert isinstance(data.get("sections"), list) and len(data["sections"]) > 0
    assert isinstance(data.get("sources"), list) and len(data["sources"]) > 0
    assert isinstance(data.get("tags"), list) and len(data["tags"]) > 0

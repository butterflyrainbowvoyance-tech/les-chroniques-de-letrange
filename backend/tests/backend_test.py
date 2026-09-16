"""Backend API tests for La Bibliothèque Secrète."""
import os
import requests
import pytest

BASE_URL = os.environ.get("REACT_APP_BACKEND_URL", "https://mystique-chronicles.preview.emergentagent.com").rstrip("/")
API = f"{BASE_URL}/api"


def test_root():
    r = requests.get(f"{API}/")
    assert r.status_code == 200
    data = r.json()
    assert data.get("app")
    assert isinstance(data.get("stories"), int) and data["stories"] > 0


def test_universes():
    r = requests.get(f"{API}/universes")
    assert r.status_code == 200
    data = r.json()
    assert len(data) == 7
    for u in data:
        assert "id" in u and "story_count" in u


def test_eras():
    r = requests.get(f"{API}/eras")
    assert r.status_code == 200
    data = r.json()
    assert len(data) == 7


def test_stories_list():
    r = requests.get(f"{API}/stories")
    assert r.status_code == 200
    data = r.json()
    assert len(data) >= 22


def test_stories_filter_universe():
    r = requests.get(f"{API}/stories", params={"universe": "arts-divinatoires"})
    assert r.status_code == 200
    data = r.json()
    assert len(data) > 0
    assert all(s["universe"] == "arts-divinatoires" for s in data)


def test_stories_search():
    r = requests.get(f"{API}/stories", params={"search": "tarot"})
    assert r.status_code == 200
    data = r.json()
    assert len(data) >= 1


def test_stories_random():
    r = requests.get(f"{API}/stories/random")
    assert r.status_code == 200
    data = r.json()
    assert "content" in data and isinstance(data["content"], list)
    assert "sources" in data and isinstance(data["sources"], list)


def test_stories_timeline():
    r = requests.get(f"{API}/stories/timeline")
    assert r.status_code == 200
    data = r.json()
    years = [d["year"] for d in data]
    assert years == sorted(years)


def test_stories_map():
    r = requests.get(f"{API}/stories/map")
    assert r.status_code == 200
    data = r.json()
    assert all("coords" in p and p["coords"] for p in data)


def test_stories_quiz():
    r = requests.get(f"{API}/stories/quiz", params={"limit": 3})
    assert r.status_code == 200
    data = r.json()
    assert len(data) == 3
    for item in data:
        assert item.get("status_key")
        assert item.get("status_meta")


def test_story_by_id_ok():
    r = requests.get(f"{API}/stories/tarot-histoire")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == "tarot-histoire"
    assert isinstance(data["content"], list)


def test_story_by_id_not_found():
    r = requests.get(f"{API}/stories/does-not-exist-xyz")
    assert r.status_code == 404


def test_ai_tell_strange_sse():
    """Verify SSE stream returns text/event-stream and yields data: lines."""
    try:
        with requests.post(
            f"{API}/ai/tell-strange",
            json={"prompt": "un objet étrange du XVIIe siècle"},
            stream=True,
            timeout=20,
        ) as r:
            assert r.status_code == 200
            ct = r.headers.get("content-type", "")
            assert "text/event-stream" in ct, f"Content-Type was {ct}"
            data_lines = 0
            for i, raw in enumerate(r.iter_lines()):
                if raw and raw.startswith(b"data:"):
                    data_lines += 1
                if data_lines >= 3 or i > 200:
                    break
            assert data_lines >= 1, "No SSE data lines received"
    except requests.exceptions.ReadTimeout:
        pytest.fail("SSE stream timed out before any data")

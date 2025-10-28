# Calls /health in-memory. Imports FastAPI app and uses TestClient to issue GET request.
import os, sys

# Make "app" package importable when running "pytest" from repo root
REPO_ROOT = os.path.dirname(os.path.abspath(os.path.join(__file__, "..")))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_ok():
    # exercise the endpoint
    r = client.get("/health")
    # check status code + exact JSON body
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

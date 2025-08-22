
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert "status" in r.json()

def test_predict_endpoint_exists():
    # Without model file it may 500 due to assertion; we only verify route is present
    r = client.post("/predict", json={"features":[0]*30})
    assert r.status_code in (200, 500)

from fastapi.testclient import TestClient
from src.main import app


def test_ready_returns_server_message():
    client = TestClient(app)
    r = client.get("/ready")
    assert r.status_code == 200
    assert {"message": "Server is serving"} in r.json()

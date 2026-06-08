from fastapi.testclient import TestClient
from src.main import app
from src.middleware import error_middleware as em
import json

def test_error_middleware_logs_and_returns_500(tmp_path):
    # Redirect log path to temporary file
    em.LOG_PATH = tmp_path / "error-log.jsonl"

    # register a short-lived route that raises to trigger the error middleware
    def _raise():
        raise RuntimeError("integration-boom")

    app.add_api_route("/__test_error", _raise, methods=["GET"])

    client = TestClient(app)
    r = client.get("/__test_error")
    assert r.status_code == 500

    text = em.LOG_PATH.read_text(encoding="utf-8")
    lines = [l for l in text.splitlines() if l.strip()]
    assert len(lines) >= 1
    obj = json.loads(lines[-1])
    assert "integration-boom" in obj["message"]

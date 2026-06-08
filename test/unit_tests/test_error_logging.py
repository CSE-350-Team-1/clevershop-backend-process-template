import json
from src.middleware import error_middleware as em


def test_log_error_writes_jsonl(tmp_path):
    # Redirect log path to temporary file
    em.LOG_PATH = tmp_path / "error-log.jsonl"

    class Ctx:
        correlation_id = "abc"
        time = 12345.0

    err = em.Error(Ctx, "boom")
    err.log_error()

    text = em.LOG_PATH.read_text(encoding="utf-8")
    lines = [l for l in text.splitlines() if l.strip()]
    assert len(lines) >= 1
    obj = json.loads(lines[-1])
    assert obj["message"] == "boom"
    assert obj["correlation_id"] == "abc"

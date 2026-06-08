from src.middleware.context_middleware import RequestContext
import uuid


def test_request_context_generates_uuid_when_invalid():
    ctx = RequestContext("not-a-uuid")
    # should produce a valid v4 UUID
    uuid.UUID(ctx.correlation_id, version=4)


def test_request_context_preserves_valid_uuid():
    valid = str(uuid.uuid4())
    ctx = RequestContext(valid)
    assert ctx.correlation_id == valid

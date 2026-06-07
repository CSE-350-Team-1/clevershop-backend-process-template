# Agents Guide for clevershop-backend-process-template

## Purpose

This repository is a backend service template for the CleverShop project. `AGENTS.md` documents how an AI agent should understand, inspect, and contribute to this repository safely and effectively.

## Repository Overview

- `run.py`: application launcher that starts the FastAPI service via Uvicorn.
- `src/main.py`: FastAPI application definition, middleware registration, and readiness endpoint.
- `src/errors/errors.py`: custom error classes.
- `src/middleware/context_middleware.py`: request context management.
- `src/middleware/error_middleware.py`: centralized exception logging and JSON response handling.
- `src/core.py`: core business logic placeholder.
- `src/tools/`: extension point for additional business utilities.
- `test/`: test directory.
- `Dockerfile`: container packaging configuration.

## Agent Responsibilities

Agents working on this repository should:

- Preserve the existing middleware pattern in `src/main.py`.
- Keep `/ready` as a reliable health check endpoint that does not require middleware.
- Add new endpoints and application behavior in `src/main.py` or new modules under `src/`.
- Add new business logic to `src/core.py` and new modules under `src/tools`.
- Keep errors logged to `logs/error-log.jsonl` using the existing `Error` logger.
    - `error-log.jsonl` file name may be changed if appropriate.
- Avoid breaking existing request flow for exempt routes listed in `EXEMPT_ROUTES`.

## Recommended Workflow

1. Read `README.md` and `src/main.py` first to understand the current service shape.
2. Use `run.py` to start the application locally:
   - `python run.py`
3. Verify the service by calling the readiness endpoint:
   - `http://localhost:8000/ready`
4. Add new features in the `src/` package and update or add tests under `test/`.
5. Ensure new endpoints either use the request context or explicitly handle the `EXEMPT_ROUTES` path exclusion rules.

## Development Notes

- The project uses FastAPI for HTTP handling.
- `RequestContext` assigns a correlation ID to each request and timestamps request start time.
- `Error.log_error()` writes JSON lines to `logs/error-log.jsonl`.
- `src/core.py` and `src/tools/` are intentionally minimal; they are the proper locations for business logic extensions, which does not exist in this template repository.

## When to Create or Modify Files

- Add new middleware under `src/middleware/` and register it in `src/main.py`.
- Add new endpoints in `src/main.py` or route modules imported by it.
- Add unit or integration tests in `test/` for new behavior.
- Keep documentation in `README.md` aligned with the actual run and container instructions.

## Notes for AI Agents

- This repository is a template, not a finished feature set.
- Prefer incremental changes that preserve structure and readability.
- Do not remove the existing error logging or request context behavior unless replacing it with a compatible implementation.
- If tests are absent, add a minimal test case for new behavior rather than leaving coverage gaps.

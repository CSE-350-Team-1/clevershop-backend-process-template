FROM python:3.12-slim

WORKDIR /app

RUN python -m pip install --no-cache-dir fastapi uvicorn

COPY run.py ./
COPY src ./src

EXPOSE 8000

ENV PORT=8000

CMD ["python", "run.py"]

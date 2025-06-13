FROM ghcr.io/astral-sh/uv:debian-slim

WORKDIR /app

# build dependencies
RUN apt-get update \
 && apt-get install -y --no-install-recommends git ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# memo dependencies
RUN apt-get update \
 && apt-get install -y --no-install-recommends espeak-ng \
 && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --locked

COPY main.py ./
COPY /src ./src/

ENV PATH="/app/.venv/bin:$PATH"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

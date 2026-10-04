FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app
RUN addgroup --system sdea && adduser --system --ingroup sdea sdea

COPY pyproject.toml README.md ./
COPY src ./src
RUN python -m pip install --upgrade pip && pip install .

USER sdea
EXPOSE 8000

CMD ["uvicorn", "tinlance_sdea.service.app:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers", "--forwarded-allow-ips=*"]

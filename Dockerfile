FROM python:3.10-slim

LABEL org.opencontainers.image.title="007-TheBond" \
      org.opencontainers.image.description="OSINT CLI toolkit for authorized security research" \
      org.opencontainers.image.source="https://github.com/Deadshot0x7/007-TheBond" \
      org.opencontainers.image.licenses="MIT" \
      org.opencontainers.image.version="v3.0"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    OSINT_OUTPUT_DIR=/app/results

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY scripts/ scripts/

RUN useradd --create-home bond && mkdir -p /app/results && chown bond /app/results
USER bond

VOLUME ["/app/results"]

CMD ["python", "scripts/007-TheBond.py"]

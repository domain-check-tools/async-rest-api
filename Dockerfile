FROM pypy:3.10-slim-bookworm AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM pypy:3.10-slim-bookworm

WORKDIR /app
EXPOSE 8000

COPY --from=builder /install /opt/pypy/

COPY entrypoint/docker-entrypoint.sh .

COPY app .

RUN chmod +x /app/docker-entrypoint.sh
ENTRYPOINT ["/app/docker-entrypoint.sh"]
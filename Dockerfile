FROM pypy:3.10-slim-bookworm AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM pypy:3.10-slim-bookworm

WORKDIR /app
EXPOSE 8000

COPY --from=builder /install /opt/pypy/

COPY script script

COPY app .

RUN find script -type f -exec chmod +x {} \;

CMD ["/app/entrypoint/docker-entrypoint.sh"]
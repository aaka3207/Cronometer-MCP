FROM python:3.12-slim

WORKDIR /app
COPY cronometer_mcp_server.py run_http_server.py ./

RUN pip install --no-cache-dir httpx "mcp>=1.2,<2"

ENV FASTMCP_HOST=0.0.0.0 \
    FASTMCP_PORT=8000

EXPOSE 8000

HEALTHCHECK --interval=60s --timeout=15s --retries=3 --start-period=10s \
  CMD ["python", "-c", "import urllib.request; r = urllib.request.urlopen('http://localhost:8000/health'); exit(0 if r.status == 200 else 1)"]
CMD ["python", "run_http_server.py"]

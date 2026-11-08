FROM python:3.12-slim

WORKDIR /app
COPY cronometer_mcp_server.py run_http_server.py ./

RUN pip install --no-cache-dir httpx "mcp>=1.2,<2"

ENV FASTMCP_HOST=0.0.0.0 \
    FASTMCP_PORT=8000

EXPOSE 8000
CMD ["python", "run_http_server.py"]

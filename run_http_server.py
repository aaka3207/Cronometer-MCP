"""Run the Cronometer MCP server over streamable HTTP for Coolify deployment."""
import os

from starlette.responses import JSONResponse

from cronometer_mcp_server import mcp

# mcp >= 1.30 defaults the FastMCP host to 127.0.0.1 and ignores the
# FASTMCP_HOST env var, and enables DNS-rebinding protection that only
# allows localhost Host headers. Both break container-to-container access
# (MetaMCP -> cronometer-mcp:8000), so set them explicitly.
mcp.settings.host = os.environ.get("FASTMCP_HOST", "0.0.0.0")
mcp.settings.port = int(os.environ.get("FASTMCP_PORT", "8000"))
mcp.settings.transport_security.allowed_hosts = [
    "cronometer-mcp:*",
    "localhost:*",
    "127.0.0.1:*",
]


@mcp.custom_route("/health", methods=["GET"])
async def health(request):
    return JSONResponse({"status": "ok"})


if __name__ == "__main__":
    mcp.run(transport="streamable-http")

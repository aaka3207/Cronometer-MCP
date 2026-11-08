"""Run the Cronometer MCP server over streamable HTTP for Coolify deployment."""
from starlette.responses import JSONResponse

from cronometer_mcp_server import mcp


@mcp.custom_route("/health", methods=["GET"])
async def health(request):
    return JSONResponse({"status": "ok"})


if __name__ == "__main__":
    mcp.run(transport="streamable-http")

"""Run the Cronometer MCP server over streamable HTTP for Coolify deployment."""
import os

from cronometer_mcp_server import mcp

if __name__ == "__main__":
    mcp.run(transport="streamable-http")

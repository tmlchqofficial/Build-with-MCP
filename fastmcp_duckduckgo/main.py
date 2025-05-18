from fastmcp import FastMCP
from duckduckgo_search import DDGS

# Create an MCP server
mcp = FastMCP("DuckDuckGo Search MCP Server", "0.1")

# Add a tool
@mcp.tool()
def duckduckgo_search(query) -> int:
    """MCP server that uses DuckDuckGo Search API"""
    results = DDGS().text(query, max_results=5)
    return results

@mcp.resource("data://config",description="Provides Data of the current running MCP server configuration as JSON")
def data_of_mcp_server() -> str:
    """Provides Data of the current running MCP server configuration as JSON."""
    return {
        "name": "DuckDuckGo Search MCP Server",
        "version": "0.1",
        "features": ["tools", "resources","prompts"],
    }

@mcp.prompt()
def ask_about_topic(topic: str) -> str:
    """Generates a user message asking for more details about a topic."""
    return f"Can you provide me more details '{topic}' so I generate a better response for you?"

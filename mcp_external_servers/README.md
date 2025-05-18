# MCP PostgreSQL Server Tutorial

This tutorial demonstrates how to use the official PostgreSQL MCP server with Claude Desktop.

https://github.com/modelcontextprotocol/servers/tree/main/src/postgres

## Prerequisites
  Before beginning, ensure the following are installed and configured:

  Docker Desktop
  Download and install from the official Docker website:
  https://docs.docker.com/desktop/

  Make sure Docker Desktop is running in the background.

  Claude Desktop
  Claude Desktop must be installed and configured to support MCP server connections.
  https://claude.ai/download

## Setup Instructions

Configure claude_desktop_config

If your configuration is empty or missing the mcpServers block, use the full snippet below.

{
  "mcpServers": {
    "postgres": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "mcp/postgres",
        "postgresql://<username>:<password>@host.docker.internal:5432/<db_name>"
      ]
    }
  }
}

If claude_desktop_config already has other MCP server configurations, simply add this postgres block inside the mcpServers section:

"postgres": {
  "command": "docker",
  "args": [
    "run",
    "-i",
    "--rm",
    "mcp/postgres",
    "postgresql://<username>:<password>@host.docker.internal:5432/<db_name>"
  ]
}

### Example Connection String
`postgresql://postgres:root@host.docker.internal:5432/RTA`

Replace:

<username> with your DB username (e.g., postgres)
<password> with your DB password (e.g., root)
<db_name> with your target database name (e.g., RTA)

### Restart Claude and Start using
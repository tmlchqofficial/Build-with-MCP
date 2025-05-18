# FastMCP Tutorial

This guide walks you through setting up and running a FastMCP server for local development and experimentation using Claude Desktop.

Note: Claude Desktop is required for this tutorial. Please install it from the official Claude Desktop Download Page. Link: https://claude.ai/download

## Setup Instructions

1. Install uv

    `https://docs.astral.sh/uv/getting-started/installation/#standalone-installer`

2. cd to the target folder and run 

    `uv init`

3. Create virtualenv with uv 

    `uv venv` & activate environment
    Windows user -> `.venv\Scripts\activate`
    Linux/Mac -> `source venv/bin/activate`

4. Install fastmcp and duckduckgo

    `uv add fastmcp==2.2.0`
    `uv add duckduckgo-search`

5. Install server

    `fastmcp install main.py`

6. Restart the claude desktop

7. Run server

    `fastmcp run main.py`

8. Dev run - To run the server in development mode

    `fastmcp dev main.py`

9. Experiment on Claude Desktop
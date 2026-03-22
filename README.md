# Claude-MCP-study-agent

A local MCP (Model Context Protocol) server built with Python to learn how to connect local tools to Claude via MCP.

## Purpose

This project was built as a hands-on way to understand how MCP works, specifically how to expose local Python functions as tools that Claude can call directly. The study planner functionality is the use case, but the real goal was learning the MCP connection flow.

## Project Structure

```
study-planner/
├── mcp_server.py   # MCP server — exposes tools via FastMCP
├── server.py       # Core logic — subject tracking, plan generation, progress
├── data.json       # Local storage
└── README.md
```

## How It Works

`server.py` contains the core study planner logic. `mcp_server.py` wraps those functions as MCP tools using [FastMCP](https://github.com/jlowin/fastmcp), making them callable by Claude.

```
Claude → MCP protocol → mcp_server.py → server.py → data.json
```

## Tools Exposed

| Tool | Description |
|------|-------------|
| `add_subject_tool` | Add a subject with a deadline (YYYY-MM-DD) |
| `generate_plan_tool` | Generate a study plan based on active subjects |
| `update_progress_tool` | Mark a subject as studied today |

## Setup

```bash
pip install fastmcp
python mcp_server.py
```

To use the CLI version directly:

```bash
python server.py
```

## Connecting to Claude Desktop

Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "study-planner": {
      "command": "python",
      "args": ["/absolute/path/to/mcp_server.py"]
    }
  }
}
```

Then restart Claude Desktop the tools will appear automatically.



from fastmcp import FastMCP
from server import add_subject, generate_plan, update_progress

mcp = FastMCP("study-planner")


# MCP TOOLS


@mcp.tool()
def add_subject_tool(name: str, deadline: str) -> str:
    """
    Add a subject with a deadline.
    Date format must be YYYY-MM-DD.
    """
    return add_subject(name, deadline)


@mcp.tool()
def generate_plan_tool() -> str:
    """
    Generate a study plan based on current subjects and deadlines.
    """
    return generate_plan()


@mcp.tool()
def update_progress_tool(subject: str) -> str:
    """
    Mark a subject as studied today.
    """
    return update_progress(subject)



# RUN MCP SERVER


if __name__ == "__main__":
    mcp.run()
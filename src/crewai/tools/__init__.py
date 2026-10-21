try:
    from .base_tool import BaseTool, tool
except Exception:
    # Defer import errors (e.g., missing typing imports in base_tool) to runtime use-sites.
    BaseTool = None
    tool = None

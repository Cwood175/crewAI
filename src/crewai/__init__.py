import warnings
import importlib
from typing import Any

# Lazily import submodules to avoid importing them at package import time.
# This prevents import-time errors from propagating during test collection.
_lazy_map = {
    "Agent": "crewai.agent.Agent",
    "Crew": "crewai.crew.Crew",
    "CrewOutput": "crewai.crews.crew_output.CrewOutput",
    "Flow": "crewai.flow.flow.Flow",
    "Knowledge": "crewai.knowledge.knowledge.Knowledge",
    "LLM": "crewai.llm.LLM",
    "BaseLLM": "crewai.llms.base_llm.BaseLLM",
    "Process": "crewai.process.Process",
    "Task": "crewai.task.Task",
    "LLMGuardrail": "crewai.tasks.llm_guardrail.LLMGuardrail",
    "TaskOutput": "crewai.tasks.task_output.TaskOutput",
}


def __getattr__(name: str) -> Any:
    """Lazy-load attributes defined in _lazy_map on demand."""
    if name in _lazy_map:
        module_path = _lazy_map[name]
        module_name, _, attr = module_path.rpartition(".")
        module = importlib.import_module(module_name)
        return getattr(module, attr)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return sorted(list(globals().keys()) + list(_lazy_map.keys()))

warnings.filterwarnings(
    "ignore",
    message="Pydantic serializer warnings:",
    category=UserWarning,
    module="pydantic.main",
)
__version__ = "0.121.0"
__all__ = [
    "Agent",
    "Crew",
    "CrewOutput",
    "Process",
    "Task",
    "LLM",
    "BaseLLM",
    "Flow",
    "Knowledge",
    "TaskOutput",
    "LLMGuardrail",
]

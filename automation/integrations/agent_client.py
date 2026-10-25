"""Explicit agent invocation interface; no live credentials in source."""
from collections.abc import Callable
from typing import Any

class AgentUnavailable(RuntimeError):
    pass

def invoke_agent(symbol: str, executor: Callable[[dict], Any] | None = None) -> dict:
    """Invoke a supplied UiPath agent executor. No mock is used in production."""
    if executor is None:
        raise AgentUnavailable("UiPath Agent Builder executor has not been configured")
    result = executor({"symbol": symbol})
    if not isinstance(result, dict):
        raise ValueError("Agent returned an invalid response type")
    return result

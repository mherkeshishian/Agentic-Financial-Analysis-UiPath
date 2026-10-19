"""Read non-secret settings. UiPath credentials belong in Orchestrator assets."""
import json
from pathlib import Path

def load_settings(path: str | Path) -> dict:
    settings = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(settings.get("queue_name"), str) or not settings["queue_name"].strip():
        raise ValueError("Missing queue_name")
    retries = settings.get("max_retries", 2)
    if isinstance(retries, bool) or not isinstance(retries, int) or not 0 <= retries <= 5:
        raise ValueError("max_retries must be 0 to 5")
    return settings

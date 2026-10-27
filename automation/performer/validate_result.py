"""Strict validation of the subset of agent output used by the performer."""
from datetime import date
import math

REQUIRED = {"symbol","summary","trend","confidence","needs_review","data_as_of"}
TRENDS = {"upward","downward","flat","unknown"}

def validate_result(result: dict, expected_symbol: str) -> dict:
    if not isinstance(result, dict) or set(result) != REQUIRED:
        raise ValueError("Unexpected agent response fields")
    if result["symbol"] != expected_symbol:
        raise ValueError("Agent symbol does not match transaction")
    if not isinstance(result["summary"], str) or not 1 <= len(result["summary"].strip()) <= 1000:
        raise ValueError("Invalid agent summary")
    if result["trend"] not in TRENDS:
        raise ValueError("Invalid trend")
    confidence=result["confidence"]
    if isinstance(confidence,bool) or not isinstance(confidence,(int,float)) or not math.isfinite(confidence) or not 0 <= confidence <= 1:
        raise ValueError("Invalid confidence")
    if not isinstance(result["needs_review"],bool):
        raise ValueError("Invalid review flag")
    try:
        date.fromisoformat(result["data_as_of"])
    except (TypeError,ValueError) as exc:
        raise ValueError("Invalid data date") from exc
    return result

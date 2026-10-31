"""Retry only transient application failures; never retry invalid business data."""
import time
from collections.abc import Callable

class TransientServiceError(RuntimeError):
    pass

def with_retry(operation: Callable[[], dict], max_retries: int = 2, sleep: Callable[[float], None] = time.sleep) -> dict:
    if not isinstance(max_retries, int) or isinstance(max_retries,bool) or not 0 <= max_retries <= 5:
        raise ValueError("max_retries must be 0 to 5")
    for attempt in range(max_retries + 1):
        try:
            return operation()
        except TransientServiceError:
            if attempt == max_retries:
                raise
            sleep(min(2 ** attempt, 8))
    raise AssertionError("unreachable")

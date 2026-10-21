"""Adapter contract between the performer and the finance MCP server.

The actual MCP transport is configured in UiPath Agent Builder; this module
provides a local deterministic execution path for integration tests.
"""
from typing import Callable

def analyze_symbol(symbol: str, get_prices: Callable[[str], dict], analyze: Callable[[list], dict]) -> dict:
    market = get_prices(symbol)
    prices = market.get("prices")
    if not isinstance(prices, list) or len(prices) < 10:
        raise ValueError("Insufficient price history")
    return {"symbol": symbol, "market_data": {"source": market.get("source"), "observations": len(prices)},
            "indicators": analyze(prices)}

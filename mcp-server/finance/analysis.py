"""Deterministic signals that an AI agent can explain with context."""
from .validation import validate_prices
from .indicators import moving_average

def analyze_trend(prices: list[float]) -> dict:
    values = validate_prices(prices, 10)
    last = values[-1]
    sma5 = moving_average(values, 5)
    sma10 = moving_average(values, 10)
    change = (last / values[0] - 1) * 100
    signal = "upward" if sma5 > sma10 else "downward" if sma5 < sma10 else "flat"
    return {"last_price": last, "sma_5": sma5, "sma_10": sma10,
            "period_change_pct": round(change, 2), "trend": signal}

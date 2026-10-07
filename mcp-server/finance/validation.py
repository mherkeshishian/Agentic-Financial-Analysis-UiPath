"""Validate untrusted symbols and request parameters."""
import math
import re
SYMBOL_PATTERN = re.compile(r"^[A-Z][A-Z0-9.\-]{0,11}$")

def validate_symbol(symbol: str) -> str:
    if not isinstance(symbol, str):
        raise ValueError("Symbol must be text")
    symbol = symbol.strip().upper()
    if not SYMBOL_PATTERN.fullmatch(symbol):
        raise ValueError("Invalid stock symbol")
    return symbol

def validate_days(days: int) -> int:
    if isinstance(days, bool) or not isinstance(days, int) or not 5 <= days <= 365:
        raise ValueError("Days must be an integer from 5 to 365")
    return days

def validate_prices(prices: list[float], min_count: int = 1) -> list[float]:
    if not isinstance(prices, list) or len(prices) < min_count or len(prices) > 365:
        raise ValueError("Invalid price series length")
    result=[]
    for value in prices:
        if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or value <= 0:
            raise ValueError("Prices must be finite positive numbers")
        result.append(float(value))
    return result

"""Simple deterministic calculations, not investment advice."""
from .validation import validate_prices

def moving_average(prices: list[float], window: int = 5) -> float:
    prices = validate_prices(prices, 1)
    if isinstance(window,bool) or not isinstance(window,int) or not 1 <= window <= len(prices):
        raise ValueError("Window must be between 1 and the number of prices")
    return round(sum(prices[-window:]) / window, 4)

def recommend(prices: list[float]) -> str:
    prices = validate_prices(prices, 5)
    return "Buy" if prices[-1] > moving_average(prices, 5) else "Hold"

"""Simple deterministic calculations, not investment advice."""
def moving_average(prices: list[float], window: int = 5) -> float:
    return sum(prices[-window:]) / window

def recommend(prices: list[float]) -> str:
    return "Buy" if prices[-1] > moving_average(prices, 5) else "Hold"

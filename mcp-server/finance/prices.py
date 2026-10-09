"""Historical price retrieval based on the original MCP Finance Server."""
import pandas as pd
import yfinance as yf
from .validation import validate_symbol, validate_days

def get_stock_prices(symbol: str, days: int = 30) -> dict:
    """Return daily closing prices with their corresponding trading dates."""
    symbol = validate_symbol(symbol)
    days = validate_days(days)
    data = yf.download(symbol, period=f"{days}d", progress=False, auto_adjust=True)
    if data is None or data.empty or "Close" not in data:
        raise ValueError(f"No market data available for {symbol}")
    closes = data["Close"]
    if isinstance(closes, pd.DataFrame):
        closes = closes.iloc[:, 0]
    closes = closes.dropna()
    if closes.empty:
        raise ValueError(f"No valid closing prices for {symbol}")
    return {"symbol": symbol, "dates": [str(d.date()) for d in closes.index], "prices": [float(p) for p in closes.tolist()], "source": "yfinance", "currency": None}

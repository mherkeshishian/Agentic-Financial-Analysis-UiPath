"""Historical price retrieval based on the original MCP Finance Server."""
import pandas as pd
import yfinance as yf
from .validation import validate_symbol, validate_days

def get_stock_prices(symbol: str, days: int = 30) -> dict:
    """Return daily closing prices with their corresponding trading dates."""
    symbol = validate_symbol(symbol)
    days = validate_days(days)
    data = yf.download(symbol, period=f"{days}d", progress=False, auto_adjust=True)
    closes = data["Close"]
    if isinstance(closes, pd.DataFrame):
        closes = closes.iloc[:, 0]
    return {"symbol": symbol.upper(), "dates": [str(d.date()) for d in closes.index], "prices": [float(p) for p in closes.tolist()]}

"""MCP entry point for financial tools. Start with `python server.py`."""
import sys
from mcp.server.fastmcp import FastMCP
from finance.prices import get_stock_prices
from finance.indicators import moving_average, recommend

mcp_finance = FastMCP("Finance")
mcp_finance.tool()(get_stock_prices)
mcp_finance.tool()(moving_average)
mcp_finance.tool()(recommend)

if __name__ == "__main__":
    print("Starting Finance MCP server...", file=sys.stderr, flush=True)
    mcp_finance.run()

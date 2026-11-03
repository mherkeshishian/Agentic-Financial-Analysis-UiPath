import json
from pathlib import Path
from automation.integrations.mcp_adapter import analyze_symbol
from automation.integrations.agent_client import invoke_agent, AgentUnavailable
from automation.performer.transaction import Transaction, TransactionState
from automation.performer.review import route_result
from automation.reporting.report import write_report
import pytest

def test_end_to_end_with_synthetic_data(tmp_path):
    prices = [float(x) for x in range(100, 112)]
    market = lambda symbol: {"symbol": symbol, "prices": prices, "source": "synthetic"}
    analysis = analyze_symbol("MSFT", market, lambda p: {"trend": "upward"})
    assert analysis["market_data"]["observations"] == 12
    fixture = json.loads((Path(__file__).parent / "fixtures/agent_result.json").read_text())
    result = invoke_agent("MSFT", lambda _: fixture)
    tx = route_result(Transaction("REQ-1001", "MSFT"), result)
    assert tx.state == TransactionState.COMPLETED
    output = write_report(tx, tmp_path)
    assert json.loads(output.read_text())["status"] == "Completed"

def test_agent_unconfigured():
    with pytest.raises(AgentUnavailable):
        invoke_agent("MSFT")

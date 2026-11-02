import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "mcp-server"))
import pytest
from finance.validation import validate_symbol, validate_prices
from finance.indicators import moving_average
from finance.analysis import analyze_trend
from automation.dispatcher.requests import FinanceRequest, read_requests
from automation.dispatcher.queue_payload import to_queue_item
from automation.performer.transaction import Transaction, TransactionState
from automation.performer.process import process_transaction
from automation.performer.review import route_result
from automation.performer.retry import with_retry, TransientServiceError
from automation.performer.validate_result import validate_result

def test_symbol_validation():
    assert validate_symbol(" msft ") == "MSFT"
    with pytest.raises(ValueError): validate_symbol("MSFT; rm -rf")

def test_price_validation():
    with pytest.raises(ValueError): validate_prices([1, float("nan")])

def test_indicators():
    assert moving_average([1, 2, 3, 4, 5], 2) == 4.5
    assert analyze_trend(list(range(1, 11)))["trend"] == "upward"

def test_queue_payload():
    req = FinanceRequest("REQ-1", "MSFT", "demo")
    assert to_queue_item(req)["specificContent"]["Symbol"] == "MSFT"

def test_csv(tmp_path):
    path=tmp_path / "requests.csv"
    path.write_text("request_id,symbol,requested_by\nR1,AAPL,demo\n")
    assert list(read_requests(path))[0].symbol == "AAPL"

def test_performer_success_and_business_error():
    good = process_transaction(Transaction("R1", "MSFT"), lambda _: {"ok": True})
    assert good.state == TransactionState.COMPLETED
    bad = process_transaction(Transaction("R2", "MSFT"), lambda _: (_ for _ in ()).throw(ValueError("invalid")))
    assert bad.state == TransactionState.BUSINESS_EXCEPTION

def test_agent_validation_and_review():
    result = {"symbol":"MSFT", "summary":"Steady trend", "trend":"upward", "confidence":0.5,
              "needs_review":False, "data_as_of":"2026-10-20"}
    assert validate_result(result, "MSFT") == result
    tx = route_result(Transaction("R1", "MSFT"), result)
    assert tx.state == TransactionState.REVIEW_REQUIRED

def test_retry():
    calls=[]
    def operation():
        calls.append(1)
        if len(calls) == 1: raise TransientServiceError("timeout")
        return {"ok":True}
    assert with_retry(operation, sleep=lambda _: None) == {"ok":True}
    assert len(calls) == 2

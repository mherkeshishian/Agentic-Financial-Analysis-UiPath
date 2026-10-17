"""Local performer core; external connectors are injected for testing."""
from collections.abc import Callable
from .transaction import Transaction, TransactionState

def process_transaction(tx: Transaction, analyze: Callable[[str], dict]) -> Transaction:
    tx.start()
    try:
        result = analyze(tx.symbol)
        if not isinstance(result, dict):
            raise TypeError("Analysis must return an object")
        tx.result = result
        tx.state = TransactionState.COMPLETED
    except ValueError as exc:
        tx.error = str(exc)
        tx.state = TransactionState.BUSINESS_EXCEPTION
    except Exception:
        tx.error = "Analysis service failed"  # No secrets or raw responses in logs.
        tx.state = TransactionState.APPLICATION_EXCEPTION
    return tx

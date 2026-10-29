"""Route low-confidence or flagged analyses for human review."""
from .transaction import Transaction, TransactionState
from .validate_result import validate_result

def route_result(tx: Transaction, agent_result: dict, threshold: float = 0.7) -> Transaction:
    if not 0 <= threshold <= 1:
        raise ValueError("Review threshold must be between 0 and 1")
    result = validate_result(agent_result, tx.symbol)
    tx.result = result
    tx.state = (TransactionState.REVIEW_REQUIRED
                if result["needs_review"] or result["confidence"] < threshold
                else TransactionState.COMPLETED)
    return tx

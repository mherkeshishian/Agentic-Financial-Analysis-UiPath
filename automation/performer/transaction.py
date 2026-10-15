"""Transaction processing state model for the UiPath performer."""
from dataclasses import dataclass, field
from enum import Enum

class TransactionState(str, Enum):
    NEW = "New"
    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"
    BUSINESS_EXCEPTION = "BusinessException"
    APPLICATION_EXCEPTION = "ApplicationException"
    REVIEW_REQUIRED = "ReviewRequired"

@dataclass
class Transaction:
    request_id: str
    symbol: str
    state: TransactionState = TransactionState.NEW
    attempts: int = 0
    error: str | None = None
    result: dict = field(default_factory=dict)

    def start(self) -> None:
        if self.state != TransactionState.NEW:
            raise ValueError("Transaction already started")
        self.state = TransactionState.IN_PROGRESS
        self.attempts += 1

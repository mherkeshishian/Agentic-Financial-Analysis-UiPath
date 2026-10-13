"""Create idempotent transaction payloads for UiPath Orchestrator."""
from .requests import FinanceRequest

def to_queue_item(request: FinanceRequest) -> dict:
    return {"reference": request.request_id,
            "priority": "Normal",
            "specificContent": {"RequestId": request.request_id,
                                "Symbol": request.symbol,
                                "RequestedBy": request.requested_by}}

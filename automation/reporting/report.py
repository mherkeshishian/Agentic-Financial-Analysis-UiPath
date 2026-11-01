"""Generate private, machine-readable transaction reports."""
import json
from pathlib import Path
from automation.performer.transaction import Transaction

def write_report(tx: Transaction, output_dir: str | Path) -> Path:
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    filename = f"{tx.request_id}.json"
    if not tx.request_id or any(c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-" for c in tx.request_id):
        raise ValueError("Unsafe request id")
    target = path / filename
    payload = {"request_id": tx.request_id, "symbol": tx.symbol, "status": tx.state.value,
               "attempts": tx.attempts, "result": tx.result, "error": tx.error}
    target.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return target

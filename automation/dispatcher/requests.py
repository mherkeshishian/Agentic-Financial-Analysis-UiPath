"""Read requests before adding transactions to an Orchestrator queue."""
import csv
from pathlib import Path
from dataclasses import dataclass
from typing import Iterator
import re

@dataclass(frozen=True)
class FinanceRequest:
    request_id: str
    symbol: str
    requested_by: str

ID_PATTERN = re.compile(r"^[A-Za-z0-9_-]{1,64}$")

def read_requests(path: str | Path) -> Iterator[FinanceRequest]:
    with open(path, newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or not {"request_id","symbol","requested_by"}.issubset(reader.fieldnames):
            raise ValueError("Missing required CSV columns")
        for line, row in enumerate(reader, start=2):
            request_id=(row.get("request_id") or "").strip()
            symbol=(row.get("symbol") or "").strip().upper()
            requester=(row.get("requested_by") or "").strip()
            if not ID_PATTERN.fullmatch(request_id) or not re.fullmatch(r"[A-Z][A-Z0-9.\-]{0,11}",symbol) or not requester:
                raise ValueError(f"Invalid request on CSV line {line}")
            yield FinanceRequest(request_id,symbol,requester)

"""Local queue-payload preview; does not call Orchestrator."""
import argparse
import json
from pathlib import Path
from automation.dispatcher.requests import read_requests
from automation.dispatcher.queue_payload import to_queue_item

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    items = [to_queue_item(req) for req in read_requests(args.csv_path)]
    result = json.dumps(items, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result + "\n", encoding="utf-8")
    else:
        print(result)

if __name__ == "__main__":
    main()

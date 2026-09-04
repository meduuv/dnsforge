from __future__ import annotations

import argparse
import json

from .core import lookup, reverse_lookup


def main() -> int:
    parser = argparse.ArgumentParser(description="DNS inspection utility")
    parser.add_argument("name")
    parser.add_argument("--type", default="A")
    parser.add_argument("--reverse", action="store_true")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    try:
        if args.reverse:
            result = reverse_lookup(args.name)
            payload = {"address": args.name, "hostname": result}
        else:
            records = lookup(args.name, args.type)
            payload = [record.__dict__ for record in records]
    except OSError as exc:
        parser.error(str(exc))
    if args.as_json:
        print(json.dumps(payload, indent=2))
    elif isinstance(payload, dict):
        print(f"{payload['address']} -> {payload['hostname']}")
    else:
        for record in payload:
            print(f"{record['type']:5} {record['name']} {record['value']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

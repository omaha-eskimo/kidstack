#!/usr/bin/env python3
"""
Simple points ledger. Run this by hand whenever a kid finishes their
checklist/mission, or redeems points for a reward.

Usage:
    python3 points.py earn gershon 25          # add 25 points
    python3 points.py redeem gershon 50 "ice cream"
    python3 points.py balance gershon
    python3 points.py balance all
"""

import json
import sys
from datetime import date
from pathlib import Path

LEDGER_PATH = Path(__file__).resolve().parent.parent / "state" / "points_ledger.json"


def load_ledger() -> dict:
    if LEDGER_PATH.exists():
        with open(LEDGER_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_ledger(ledger: dict) -> None:
    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2)


def balance(ledger: dict, kid: str) -> int:
    entries = ledger.get(kid, [])
    return sum(e["amount"] for e in entries)


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print(__doc__)
        return

    action, kid = args[0], args[1]
    ledger = load_ledger()
    ledger.setdefault(kid, [])

    if action == "earn":
        amount = int(args[2])
        ledger[kid].append({"date": date.today().isoformat(), "amount": amount, "note": "earned"})
        save_ledger(ledger)
        print(f"{kid}: +{amount} points. New balance: {balance(ledger, kid)}")

    elif action == "redeem":
        amount = int(args[2])
        note = args[3] if len(args) > 3 else "redeemed"
        ledger[kid].append({"date": date.today().isoformat(), "amount": -amount, "note": note})
        save_ledger(ledger)
        print(f"{kid}: -{amount} points ({note}). New balance: {balance(ledger, kid)}")

    elif action == "balance":
        if kid == "all":
            for k in ledger:
                print(f"{k}: {balance(ledger, k)} points")
        else:
            print(f"{kid}: {balance(ledger, kid)} points")

    else:
        print(__doc__)


if __name__ == "__main__":
    main()

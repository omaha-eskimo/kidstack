#!/usr/bin/env python3
"""
Check whether today is a "print day" by parsing an iCal (.ics) file that
marks custody or schedule blocks.

Convention: events whose SUMMARY starts with a configured prefix (default
"Print ||") mark days the gazette should print. Events starting with a
second prefix (default "Skip ||") mark days to skip.

Set the calendar path and prefixes in environment variables, or pass them
directly to kids_with_alex().

Environment variables:
    GAZETTE_CALENDAR_PATH   path to your .ics file (default: ~/gazette.ics)
    GAZETTE_PRINT_PREFIX    summary prefix for print days (default: "Print ||")
    GAZETTE_SKIP_PREFIX     summary prefix for skip days  (default: "Skip ||")

Usage as a module:
    from calendar_check import kids_with_alex
    if not kids_with_alex():
        sys.exit(0)

Usage as a script:
    python3 calendar_check.py        # exits 0 if print day, 1 if skip day
"""

from __future__ import annotations

import os
import re
import sys
from datetime import date, timedelta
from pathlib import Path

DEFAULT_CALENDAR_PATH = Path.home() / "gazette.ics"
DEFAULT_PRINT_PREFIX = "Print ||"
DEFAULT_SKIP_PREFIX = "Skip ||"


def _parse_date(s: str) -> date | None:
    s = s.strip()
    if len(s) == 8 and s.isdigit():
        return date(int(s[:4]), int(s[4:6]), int(s[6:8]))
    return None


def _expand_rrule(start: date, end: date, rrule: str, horizon: date) -> list[tuple[date, date]]:
    """Expand a simple RRULE into (start, end) pairs up to horizon."""
    duration = (end - start).days
    occurrences = [(start, end)]

    freq_match = re.search(r'FREQ=(\w+)', rrule)
    interval_match = re.search(r'INTERVAL=(\d+)', rrule)
    until_match = re.search(r'UNTIL=(\d{8})', rrule)
    count_match = re.search(r'COUNT=(\d+)', rrule)

    if not freq_match:
        return occurrences

    freq = freq_match.group(1)
    interval = int(interval_match.group(1)) if interval_match else 1
    until = _parse_date(until_match.group(1)) if until_match else horizon
    count = int(count_match.group(1)) if count_match else 9999

    if freq == 'WEEKLY':
        delta = timedelta(weeks=interval)
    elif freq == 'DAILY':
        delta = timedelta(days=interval)
    else:
        return occurrences

    current = start + delta
    i = 1
    while current <= min(until, horizon) and i < count:
        occurrences.append((current, current + timedelta(days=duration)))
        current += delta
        i += 1

    return occurrences


def kids_with_alex(
    today: date | None = None,
    calendar_path: Path | None = None,
    print_prefix: str | None = None,
    skip_prefix: str | None = None,
) -> bool:
    """Return True if today is a print day, False if a skip day, True if unknown."""
    if today is None:
        today = date.today()

    path = calendar_path or Path(os.environ.get("GAZETTE_CALENDAR_PATH", str(DEFAULT_CALENDAR_PATH)))
    p_prefix = print_prefix or os.environ.get("GAZETTE_PRINT_PREFIX", DEFAULT_PRINT_PREFIX)
    s_prefix = skip_prefix or os.environ.get("GAZETTE_SKIP_PREFIX", DEFAULT_SKIP_PREFIX)

    if not path.exists():
        return True  # default to printing if calendar not found

    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    horizon = today + timedelta(days=1)
    print_ranges: list[tuple[date, date]] = []
    skip_ranges: list[tuple[date, date]] = []

    for event_text in content.split('BEGIN:VEVENT'):
        summary_match = re.search(r'SUMMARY:(.+)', event_text)
        if not summary_match:
            continue
        summary = summary_match.group(1).strip()

        is_print = summary.startswith(p_prefix)
        is_skip = summary.startswith(s_prefix)
        if not is_print and not is_skip:
            continue

        dtstart_match = re.search(r'DTSTART[^:]*:(\d{8})', event_text)
        dtend_match = re.search(r'DTEND[^:]*:(\d{8})', event_text)
        if not dtstart_match:
            continue

        start = _parse_date(dtstart_match.group(1))
        end = _parse_date(dtend_match.group(1)) if dtend_match else (start + timedelta(days=1))
        if not start:
            continue

        rrule_match = re.search(r'RRULE:(\S+)', event_text)
        ranges = _expand_rrule(start, end, rrule_match.group(1), horizon) if rrule_match else [(start, end)]

        if is_print:
            print_ranges.extend(ranges)
        else:
            skip_ranges.extend(ranges)

    def in_range(d: date, ranges: list[tuple[date, date]]) -> bool:
        return any(s <= d < e for s, e in ranges)

    if in_range(today, print_ranges):
        return True
    if in_range(today, skip_ranges):
        return False
    return True  # default: print


if __name__ == '__main__':
    result = kids_with_alex()
    if result:
        print("Print day.")
        sys.exit(0)
    else:
        print("Skip day.")
        sys.exit(1)

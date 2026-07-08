#!/usr/bin/env python3
"""
Daily Kid Gazette generator.

Picks the next culture bite + mission from each kid's content bank (cycling
through without repeats until the bank is exhausted, then reshuffling),
renders the newspaper template, converts it to PDF, prints it, and archives
a dated copy.

Usage:
    python3 generate.py gershon
    python3 generate.py maetav
    python3 generate.py all              # both kids
    python3 generate.py gershon --no-print   # generate only, skip printing
"""

from __future__ import annotations

import json
import random
import subprocess
import sys
import shutil
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from calendar_check import kids_with_alex

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content_bank"
TEMPLATE_DIR = ROOT / "templates"
STATE_DIR = ROOT / "state"
ARCHIVE_DIR = ROOT / "archive"
OUTPUT_DIR = ROOT / "output"

TYPE_LABELS = {
    "quote": "Words to Live By",
    "story": "Story Corner",
    "riddle": "Riddle of the Day",
}


def load_json(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_state(kid: str) -> dict:
    state_path = STATE_DIR / f"{kid}_state.json"
    if state_path.exists():
        state = load_json(state_path)
        # Ensure new rotation keys exist in old state files
        for key in ("cm_order", "cm_pos", "read_order", "read_pos",
                    "listen_order", "listen_pos", "journal_order", "journal_pos"):
            if key not in state:
                state[key] = [] if key.endswith("order") else 0
        return state
    return {"edition_number": 0,
            "culture_order": [], "culture_pos": 0,
            "mission_order": [], "mission_pos": 0,
            "cm_order": [], "cm_pos": 0,
            "read_order": [], "read_pos": 0,
            "listen_order": [], "listen_pos": 0,
            "journal_order": [], "journal_pos": 0}


def next_item(bank: list, order_key: str, pos_key: str, state: dict) -> dict:
    """Cycle through a content bank without repeats; reshuffle when exhausted."""
    if not state[order_key] or state[pos_key] >= len(state[order_key]):
        order = list(range(len(bank)))
        random.shuffle(order)
        state[order_key] = order
        state[pos_key] = 0
    idx = state[order_key][state[pos_key]]
    state[pos_key] += 1
    return bank[idx]


def render_newspaper(kid: str) -> Path:
    bank = load_json(CONTENT_DIR / f"{kid}.json")
    state = load_state(kid)

    state["edition_number"] += 1
    culture = next_item(bank["culture_bites"], "culture_order", "culture_pos", state)
    mission = next_item(bank["missions"], "mission_order", "mission_pos", state)

    cm_activity = None
    i_can_read = None
    listening = None
    journal_prompt = None
    if "cm_activities" in bank:
        cm_activity = next_item(bank["cm_activities"], "cm_order", "cm_pos", state)
    if "i_can_read" in bank:
        i_can_read = next_item(bank["i_can_read"], "read_order", "read_pos", state)
    if "listening" in bank:
        listening = next_item(bank["listening"], "listen_order", "listen_pos", state)
    if "journal_prompts" in bank:
        journal_prompt = next_item(bank["journal_prompts"], "journal_order", "journal_pos", state)

    save_json(STATE_DIR / f"{kid}_state.json", state)

    checklist = bank["checklist"]
    afternoon_routine = bank.get("afternoon_routine", [])
    morning_routine = bank.get("morning_routine", [])

    max_points = (mission["points"]
                  + sum(c["points"] for c in checklist)
                  + sum(c["points"] for c in afternoon_routine)
                  + sum(c["points"] for c in morning_routine))

    culture_label = ("Read with Mom" if cm_activity
                     else TYPE_LABELS.get(culture["type"], "Today's Reading"))

    env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))
    template = env.get_template("newspaper.html")

    html = template.render(
        masthead=bank["masthead"],
        masthead_title=bank.get("masthead_title", ""),
        tagline=bank["tagline"],
        accent_color=bank["accent_color"],
        kid_name=bank["kid_name"],
        date_str=date.today().strftime("%A, %B %-d, %Y"),
        edition_number=state["edition_number"],
        culture={**culture, "type_label": culture_label},
        mission=mission,
        checklist=checklist,
        afternoon_routine=afternoon_routine,
        morning_routine=morning_routine,
        cm_activity=cm_activity,
        i_can_read=i_can_read,
        listening=listening,
        journal_prompt=journal_prompt,
        max_points=max_points,
    )

    OUTPUT_DIR.mkdir(exist_ok=True)
    html_path = OUTPUT_DIR / f"{kid}_today.html"
    html_path.write_text(html, encoding="utf-8")
    return html_path


def html_to_pdf(html_path: Path, kid: str) -> Path | None:
    pdf_path = html_path.with_suffix(".pdf")

    if shutil.which("wkhtmltopdf"):
        subprocess.run(
            ["wkhtmltopdf", "--enable-local-file-access", "--quiet",
             str(html_path), str(pdf_path)],
            check=True,
        )
        return pdf_path

    # Fallback: headless Chrome / Chromium, if installed
    for chrome_bin in ("google-chrome", "chromium", "chromium-browser",
                        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"):
        if shutil.which(chrome_bin) or Path(chrome_bin).exists():
            subprocess.run(
                [chrome_bin, "--headless", "--disable-gpu",
                 f"--print-to-pdf={pdf_path}", str(html_path)],
                check=True,
            )
            return pdf_path

    print("WARNING: no PDF converter found (wkhtmltopdf or Chrome). "
          "HTML file saved, but not converted to PDF or printed.")
    return None


def print_pdf(pdf_path: Path, printer_name: str | None) -> None:
    cmd = ["lpr"]
    if printer_name:
        cmd += ["-P", printer_name]
    cmd.append(str(pdf_path))
    subprocess.run(cmd, check=True)


def archive_copy(src_path: Path, kid: str) -> None:
    ARCHIVE_DIR.mkdir(exist_ok=True)
    dest = ARCHIVE_DIR / f"{kid}_{date.today().isoformat()}{src_path.suffix}"
    shutil.copy(src_path, dest)


def run_for_kid(kid: str, do_print: bool, printer_name: str | None) -> None:
    html_path = render_newspaper(kid)
    print(f"[{kid}] rendered {html_path}")

    pdf_path = html_to_pdf(html_path, kid)
    if pdf_path:
        archive_copy(pdf_path, kid)
        print(f"[{kid}] archived {pdf_path.name}")
        if do_print:
            print_pdf(pdf_path, printer_name)
            print(f"[{kid}] sent to printer" + (f" ({printer_name})" if printer_name else ""))
    else:
        archive_copy(html_path, kid)


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)

    target = args[0]
    do_print = "--no-print" not in args
    force = "--force" in args  # bypass calendar check

    # Optional: python3 generate.py gershon --printer "HP_OfficeJet"
    printer_name = None
    if "--printer" in args:
        printer_name = args[args.index("--printer") + 1]

    if not force and not kids_with_alex():
        print("Kids are with Noah today — skipping. Pass --force to override.")
        sys.exit(0)

    kids = ["gershon", "maetav"] if target == "all" else [target]
    for kid in kids:
        run_for_kid(kid, do_print, printer_name)

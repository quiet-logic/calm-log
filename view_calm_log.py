# view_calm_log.py — JSONL viewer (portable)

from __future__ import annotations
import json
import os
import sys

LOG_PATH = os.path.join(os.path.dirname(__file__), "calm_log.jsonl")

def load_all() -> list[dict]:
    try:
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            return [json.loads(line) for line in f if line.strip()]
    except FileNotFoundError:
        return []

def print_entry(e: dict) -> None:
    mood = f" [{e['mood']}]" if e.get("mood") else ""
    tags = " " + " ".join(f"#{t}" for t in (e.get("tags") or []))
    print(f"{e['ts']}{mood}{tags} — {e['text']}")

def view_last(n: int = 5) -> None:
    items = load_all()
    if not items:
        print("No entries yet.")
        return
    for e in items[-n:]:
        print_entry(e)

def search_text(q: str) -> None:
    items = load_all()
    ql = q.lower()
    hits = [e for e in items if ql in e.get("text", "").lower()]
    if not hits:
        print("No matches.")
        return
    for e in hits:
        print_entry(e)

def filter_mood(m: str) -> None:
    items = load_all()
    hits = [e for e in items if (e.get("mood") or "").lower() == m.lower()]
    if not hits:
        print("No entries for that mood.")
        return
    for e in hits:
        print_entry(e)

def filter_tag(tag: str) -> None:
    items = load_all()
    hits = [e for e in items if tag.lower() in [t.lower() for t in (e.get("tags") or [])]]
    if not hits:
        print("No entries with that tag.")
        return
    for e in hits:
        print_entry(e)

def usage() -> None:
    print(
        "Usage:\n"
        "  python3 view_calm_log.py last [N]\n"
        '  python3 view_calm_log.py search "text..."\n'
        "  python3 view_calm_log.py mood tired\n"
        "  python3 view_calm_log.py tag focus\n"
    )

def main(argv: list[str]) -> None:
    if len(argv) < 2:
        view_last(5)  # default: show last 5
        return
    cmd = argv[1].lower()
    if cmd == "last":
        n = int(argv[2]) if len(argv) > 2 and argv[2].isdigit() else 5
        view_last(n)
    elif cmd == "search" and len(argv) >= 3:
        search_text(" ".join(argv[2:]))
    elif cmd == "mood" and len(argv) >= 3:
        filter_mood(argv[2])
    elif cmd == "tag" and len(argv) >= 3:
        filter_tag(argv[2])
    else:
        usage()

if __name__ == "__main__":
    main(sys.argv)

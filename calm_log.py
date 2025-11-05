# calm_log.py — JSONL logger (portable)

from __future__ import annotations
from datetime import datetime
import json
import os

LOG_PATH = os.path.join(os.path.dirname(__file__), "calm_log.jsonl")

def timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def save_entry(entry: dict) -> None:
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

def read_last(n: int = 5) -> list[dict]:
    try:
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()[-n:]
        return [json.loads(line) for line in lines if line.strip()]
    except FileNotFoundError:
        return []

def prompt_log() -> None:
    text = input("One small calming moment or win? ").strip()
    if not text:
        print("No worries — nothing logged today. Be kind to yourself.")
        return
    mood = input("Mood (optional, e.g., tired/good/stressed): ").strip() or None
    tags_raw = input("Tags (comma-separated, optional): ").strip()
    tags = [t.strip() for t in tags_raw.split(",") if t.strip()] or None
    entry = {"ts": timestamp(), "text": text, "mood": mood, "tags": tags}
    save_entry(entry)
    print("Saved. Slow is smooth. You're doing great 🕯️")

def show_last(n: int) -> None:
    items = read_last(n)
    if not items:
        print("No entries yet. First calm moment awaits 🌱")
        return
    print(f"--- Recent {min(n, len(items))} calm moments ---")
    for e in items:
        mood = f" [{e['mood']}]" if e.get("mood") else ""
        tags = " " + " ".join(f"#{t}" for t in (e.get("tags") or []))
        print(f"{e['ts']}{mood}{tags} — {e['text']}")

def main() -> None:
    print("Calm Moments Logger 🌿")
    while True:
        ch = input("\n[L]og  [V]iew last  [Q]uit → ").strip().lower()
        if ch == "q":
            print("Goodbye. Slow is smooth 🕯️")
            return
        elif ch == "v":
            raw = input("How many to show? (Enter for 5) ").strip()
            n = int(raw) if raw.isdigit() else 5
            show_last(n)
        elif ch == "l":
            prompt_log()
        else:
            print("Try L, V, or Q 🙂")

if __name__ == "__main__":
    main()

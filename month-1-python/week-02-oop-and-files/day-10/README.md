# Day 10: JSON Persistence, Pathlib & Datetime

## Learning Objectives
1. The `json` module: `json.dumps()` / `json.loads()` (strings) vs `json.dump()` / `json.load()` (files).
2. Serializing Python objects & dataclasses into JSON dictionaries (`asdict()`).
3. Modern file paths using Python's `pathlib.Path` (goodbye messy string paths).
4. Generating timestamps and calculating time deltas with `datetime`.
5. Defensive JSON error handling (`json.JSONDecodeError`).

---

## Daily Task: Persistent Task Manager with JSON & Dates (Without AI)
Upgrade Day 9's Task model to persist data to a JSON file:
1. `Task` dataclass:
   - `id: int`
   - `title: str`
   - `is_completed: bool = False`
   - `created_at: str` (defaults to current UTC/local ISO timestamp, e.g. `datetime.now().isoformat()`)
2. `TaskManager` class:
   - Manages list of tasks.
   - `save_to_json(file_path: Path) -> None`: serializes tasks to clean JSON (`indent=2`).
   - `load_from_json(file_path: Path) -> None`: loads tasks from JSON file.
   - **Defensive resilience:**
     - If file doesn't exist, initializes empty without crashing.
     - If JSON is corrupted/malformed, catches `json.JSONDecodeError` and handles it safely.
3. Interactive CLI or script demonstration adding 2 tasks, saving to `tasks.json`, and reloading.

---

## Developer English Task: Serialization & Daily Standup
1. Explain what **"Serialization"** and **"Deserialization"** mean in plain English.
2. Deliver a 3-bullet **Daily Standup Update** (Yesterday, Today, Blockers).


# Day 14: Week 2 Capstone Project & Closed-Book Examination

## Project Objective: CLI GitHub Issue & Habit Tracker with Pytest
Build a production-grade, modular CLI application from scratch that combines everything mastered in Week 2:
- OOP & Classes with `__str__` (Day 8)
- Type Hints, `@dataclass` & Composition (Day 9)
- JSON Persistence with `pathlib.Path` & `datetime` (Day 10)
- Generators & Custom Sorting with `lambda` (Day 11)
- Automated Unit Testing with `pytest` & Fixtures (Day 12)
- External REST API Integration with `requests` (Day 13)

---

## Technical Specifications

### Architecture Layout:
```text
day-14-capstone/
├── tracker.py       # Core classes: Issue, IssueManager
├── test_tracker.py  # Pytest test suite (at least 4 automated tests)
└── issues.json      # Saved issues persistent store
```

### 1. `Issue` Dataclass (`@dataclass`):
- `id: int`
- `title: str`
- `category: str` (e.g., "Bug", "Feature", "Docs")
- `is_closed: bool = False`
- `created_at: str` (ISO format timestamp)

### 2. `IssueManager` Class (Composition):
- `__init__(self, storage_path: Path)`
- `add_issue(self, title: str, category: str) -> Issue`
- `close_issue(self, issue_id: int) -> bool` (marks closed, returns True if found, False otherwise)
- `stream_open_issues(self)`: **A generator using `yield`** that yields open issues one by one.
- `save_to_json(self) -> None`: serializes issues using `asdict()` and `json.dump(..., indent=2)`.
- `load_from_json(self) -> None`: rehydrates `Issue` objects using `Issue(**item)`. Handles `FileNotFoundError` and `JSONDecodeError`.
- `fetch_github_user_profile(self, username: str) -> dict | None`: calls GitHub API with `timeout=5`.

### 3. Automated Test Suite (`test_tracker.py`):
Write at least 4 unit tests using `pytest`:
1. Test adding an issue.
2. Test closing an issue.
3. Test generator streaming only open issues.
4. Test saving and loading with JSON persistence using a temporary test file.

---

## Rules
- **No AI generation** — write this independently.
- Clean functions, proper type hints, and exception handling.


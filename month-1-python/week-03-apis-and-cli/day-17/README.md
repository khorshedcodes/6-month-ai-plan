# Day 17: Production CLI Tools with `argparse` & Structured Logging

## Learning Objectives
1. Why professional command-line tools avoid `input()` and use CLI flags (`--help`, `--limit 5`).
2. The standard library `argparse` module: positional arguments, optional flags, type validation, and automatic `--help`.
3. The fatal flaws of using `print()` in production code.
4. Python's built-in `logging` module: Log Levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).
5. Formatting logs with timestamps, file origins, and severity levels.
6. Directing logs to both the terminal (stdout) and a log file simultaneously.

---

## Daily Task: Production CLI Article / GitHub Inspector (Without AI)
Build a standalone CLI tool in `fetcher.py`:
1. Use `argparse` to parse command-line options:
   - Positional or optional argument: `--user` (GitHub username, required).
   - Optional argument: `--limit` (integer, default `5`, max repos to list).
   - Flag: `--verbose` (boolean flag `action="store_true"` that enables `DEBUG` logging).
2. Configure structured logging:
   - Format: `[%(asctime)s] [%(levelname)s] %(message)s`
   - Default log level: `INFO` (or `DEBUG` if `--verbose` is passed).
3. Fetch user repositories via `https://api.github.com/users/{username}/repos?per_page={limit}`:
   - Log `INFO`: *"Fetching top %(limit)s repos for %(user)s..."*
   - Log `DEBUG`: *"HTTP request sent to GitHub API with timeout=5s"*
   - Log `ERROR`: If network or API fails.
4. Print clean formatted repo output to console.

---

## Developer English Task: Architectural Comparison
Explain in 3-4 professional sentences:
*"Why is the Python `logging` module required in production systems instead of standard `print()` statements?"*

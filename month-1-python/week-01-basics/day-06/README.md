# Day 6: Exception Handling, Modules & Virtual Environments

## Learning Objectives
1. Exception handling: `try`, `except`, `else`, `finally`.
2. Catching specific exceptions (`ValueError`, `FileNotFoundError`, `ZeroDivisionError`).
3. Raising custom exceptions (`raise ValueError(...)`).
4. Creating multi-file Python modules (`import analyzer`).
5. Virtual environments (`python -m venv .venv`) and `requirements.txt`.

---

## Daily Task: Modular, Resilient Log Analyzer (Without AI)
Refactor Day 5's log analyzer into 2 separate modules:
1. `analyzer.py`:
   - Contains a function `parse_log_file(file_path)` that handles `FileNotFoundError` gracefully and returns parsed stats.
   - Raises a custom error if the log file is completely empty.
2. `main.py`:
   - Imports `analyzer`.
   - Prompts the user for the log file path.
   - Wraps the call in a `try/except` block and prints a clean user-friendly error message if anything goes wrong (no ugly tracebacks).

---

## Developer English Task: Setup Guide (`README.md`)
Write a professional `README.md` explaining how another developer can:
1. Clone the repo
2. Create and activate a Python virtual environment (`.venv`)
3. Run the script


# Day 5: Strings, List Comprehensions & File Handling

## Learning Objectives
1. Essential string methods: `.strip()`, `.split()`, `.join()`, `.startswith()`, `.replace()`.
2. List comprehensions: concise, idiomatic Python vs loops.
3. File I/O: The `with open(..., mode)` context manager (`"r"`, `"w"`, `"a"`).
4. Iterating through files line by line efficiently.

---

## Daily Task: Log File Analyzer (Without AI)
Build a script that:
1. Reads a sample log file (`app.log`).
2. Parses each line to count log levels (`[INFO]`, `[WARN]`, `[ERROR]`).
3. Extracts all `[ERROR]` messages into a clean list using a list comprehension or filtering.
4. Writes a summary report (`summary.txt`) containing:
   - Total lines processed
   - Counts for INFO, WARN, ERROR
   - List of error messages found

---

## Developer English Task: Writing a Bug Report
Write a professional GitHub-style bug report describing what happens if `app.log` does not exist when the script runs.
- **Title**
- **Description / Context**
- **Steps to Reproduce**
- **Expected vs Actual Behavior**


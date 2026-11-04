# Day 5: Notes & Developer English Practice

## Topic: Strings, List Comprehensions, File I/O & Bug Reporting

---

## 1. Key Concept Summary
- **List Comprehension Syntax:** `[expression for item in iterable if condition]`
- **File Modes:**
  - `"w"` (Write): Truncates (erases) existing content and writes fresh.
  - `"a"` (Append): Preserves existing content and appends to the end.
- **Context Manager (`with`):** Guarantees proper acquisition and release of operating system resources (file descriptors), preventing memory/file leaks even when runtime exceptions occur.
- **Working Directory Trap:** Relative file paths (`"app.log"`) resolve against the terminal's *current working directory*, not the script's folder location. Use `os.path` or `pathlib` for location-independent path resolution.

---

## 2. Professional Bug Report Practice

### Student's Raw Draft:
> **Bug:** File not found error in code.py  
> **Description:** When run the file in the with open function there is file not found error for the file "app.log"  
> **Steps to Reproduce:**  
> 1. Open terminal at F:\6 month plan \  
> 2. Run command : python month-1python/week-01/basics/day-05/code.py  
> 3. Observe output  
> **Expected Behavior:** Run without error and print("Analysis complete")  
> **Actual Behavior:** FileNotFoundError  

### Polished Version (For GitHub Issues & Jira Tickets):
> ### Bug: `FileNotFoundError` when executing `code.py` from repository root
>
> **Description:**
> Executing `code.py` using relative file paths fails with a `FileNotFoundError: [Errno 2] No such file or directory: 'app.log'` when invoked outside the `day-05` directory.
>
> **Steps to Reproduce:**
> 1. Open terminal at project root (`F:\6 month plan`).
> 2. Execute: `python month-1-python/week-01-basics/day-05/code.py`.
> 3. Observe console output.
>
> **Expected Behavior:**
> The script should locate `app.log` relative to its own script directory, process all log lines, and generate `summary.txt` successfully.
>
> **Actual Behavior:**
> Script crashes immediately with `FileNotFoundError: No such file or directory: 'app.log'`.
>
> **Suggested Fix:**
> Resolve the file path dynamically using `pathlib.Path(__file__).parent / "app.log"` or `os.path.dirname(os.path.abspath(__file__))`.

---

## 3. Useful Tech Vocabulary Learned
- **Context Manager:** Python construct that handles setup and teardown (`__enter__` and `__exit__`), used via `with`.
- **Truncate:** To empty or wipe clean an existing file before writing.
- **Current Working Directory (CWD):** The folder from which a shell process was launched.
- **Reproduce:** To perform the exact steps necessary to trigger a specific bug.


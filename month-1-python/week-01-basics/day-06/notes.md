# Day 6: Notes & Developer English Practice

## Topic: Exceptions, Modules, Virtual Environments & Setup Guides

---

## 1. Exception Handling Architecture Mastered
- **Specific Exception Handling:** Catch explicit exceptions (`FileNotFoundError`, `ValueError`, `KeyError`) instead of catching `Exception` or using bare `except: pass`.
- **The `try / except / else / finally` flow:**
  - `try`: Code that might raise an exception.
  - `except ExceptionType:` Code that recovers from that specific exception.
  - `else`: Executes **only** when the `try` block succeeds without any exceptions.
  - `finally`: Executes unconditionally, ideal for closing database connections, sockets, or file handles.
- **The Bare `except: pass` Anti-Pattern:** Silently swallowing all exceptions hides syntax errors, typos, and system signals (like `KeyboardInterrupt` / Ctrl+C), making debugging nearly impossible.

---

## 2. Professional Developer English: Project Setup Guide (`README.md`)

### Student's Raw Draft:
> 1. Virtual Environment: python -m venv .venv  
> 2. Dependencies : pip install -r requirements.txt  
> 3. Running the Script : .env/Scripts/activate  

### Polished Version (For GitHub / Production Repositories):
```markdown
## Getting Started

### 1. Create and Activate Virtual Environment
Create an isolated Python virtual environment to manage project-specific dependencies:

```bash
# Create virtual environment
python -m venv .venv

# Activate on Windows (PowerShell/CMD):
.venv\Scripts\activate

# Activate on macOS/Linux:
source .venv/bin/activate
```

### 2. Install Dependencies
Install all pinned project dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the Application
Execute the main entry point and provide a path to a valid log file when prompted:

```bash
python main.py
```
```

---

## 3. Useful Tech Vocabulary Learned
- **Virtual Environment (`venv`):** An isolated runtime directory that keeps project dependencies separated from system-level Python.
- **Dependency Isolation:** Ensuring different projects can use incompatible package versions simultaneously on the same machine.
- **Entry Point:** The primary script or function where application execution begins (`main.py`).
- **Graceful Failure:** When a program encounters an unexpected error and reports a readable message instead of crashing with a stack trace.


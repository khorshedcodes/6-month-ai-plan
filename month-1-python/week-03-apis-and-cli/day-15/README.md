# Day 15: Decorators, Closures & Custom Context Managers

## Learning Objectives
1. Higher-order functions in Python: functions as first-class citizens (passed as args, returned from functions).
2. Closures: functions capturing variables from outer scopes.
3. Decorators: the `@decorator` syntax, `*args`, and `**kwargs`.
4. The `@functools.wraps` decorator for preserving metadata.
5. Practical production decorators: `@timer` (latency benchmarking) and `@retry` (resilient API calls).
6. Custom Context Managers with `__enter__` and `__exit__`.

---

## Daily Task: Performance & Reliability Decorators (Without AI)
Build two reusable production decorators in `decorators.py`:
1. `@timer`:
   - Measures execution time using `time.perf_counter()`.
   - Prints: `"[TIMER] function_name took 0.0452s to execute."`
   - Returns the original function's return value.
2. `@retry(max_attempts=3, delay=1.0)`:
   - Takes decorator arguments (`max_attempts`).
   - If the wrapped function raises an exception, catches it, waits `delay` seconds, and retries.
   - If attempts run out, raises the final exception.
3. In `demo.py`:
   - Apply `@timer` to a CPU-bound or simulated slow task.
   - Apply `@retry(max_attempts=3)` to an unstable network or mock API function.

---

## Developer English Task: Technical Explanations
Explain in 3-4 professional sentences:
*"What is a decorator in Python, and how does it help follow the DRY (Don't Repeat Yourself) principle in production systems?"*


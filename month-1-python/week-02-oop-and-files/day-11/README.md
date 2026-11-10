# Day 11: Iterators, Generators (`yield`), Lambdas & Custom Sorting

## Learning Objectives
1. The iterator protocol: `iter()` and `next()`.
2. Generator functions with `yield`: lazy evaluation vs. eager evaluation.
3. Memory comparison: streaming 1 million items with a generator vs loading a giant list into RAM.
4. Anonymous functions: `lambda` syntax.
5. High-performance sorting: `sorted(iterable, key=..., reverse=...)`.

---

## Daily Task: Memory-Efficient Large-Log Processor & Ranked Search (Without AI)
Build a data processing script:
1. `generate_mock_logs(file_path, num_lines=1000)`:
   - Creates a synthetic log file with randomized levels (`[INFO]`, `[WARN]`, `[ERROR]`), timestamps, and mock error codes.
2. `stream_error_logs(file_path)`:
   - A **generator function** using `yield` that streams only lines containing `[ERROR]` one by one without loading the entire file into a list.
3. Ranking & Sorting with `lambda`:
   - Parse extracted errors into objects or dicts with `error_code` and `latency_ms`.
   - Sort errors by `latency_ms` descending (highest latency first) using `sorted(..., key=lambda x: ...)`.
   - Print the Top 5 slowest errors.

---

## Developer English Task: Explaining Performance Trade-offs
Explain in 3-4 professional sentences:
*"Why are generator functions (`yield`) essential when processing massive datasets or streaming real-time AI responses compared to returning standard Python lists?"*


# Day 22: NumPy Fundamentals (Arrays, Shapes, Vectorization & Broadcasting)

## Learning Objectives
1. Why Python lists are too slow for AI and data science (memory layout, pointer indirection).
2. The NumPy `ndarray`: contiguous memory allocation in C, fixed `dtype`.
3. Array attributes: `.shape`, `.ndim`, `.size`, `.dtype`.
4. Vectorization: replacing Python `for` loops with C-speed parallel mathematical operations.
5. Broadcasting rules: how NumPy performs arithmetic between arrays of different shapes.
6. Boolean masking and indexing (e.g. `arr[arr > 5]`).

---

## Daily Task: Vectorization vs. Python Loop Benchmark Engine (Without AI)
In `numpy_benchmark.py`:
1. Generate an array of 1,000,000 random floating point numbers.
2. Operation: multiply each element by 2.5 and add 10.0.
3. Measure execution time with a traditional Python `for` loop.
4. Measure execution time with vectorized NumPy syntax (`arr * 2.5 + 10.0`).
5. Print the benchmark results and calculate the exact speedup factor (e.g., NumPy is 50x–100x faster!).
6. Implement a matrix normalizer: given a 2D matrix ($5 \times 3$), normalize each column to have zero mean using NumPy broadcasting: `X_norm = X - X.mean(axis=0)`.

---

## Developer English Task: Explaining Vectorization (C1 & Level 75)
Explain why NumPy array operations are orders of magnitude faster than standard Python `for` loops.

---

## Mandarin Chinese Task: Lesson 5 (Days of the Week & Schedule)
Learn how to say the days of the week in Mandarin:
- `星期一` (*xīngqīyī* = Monday) ... `星期日/星期天` (*xīngqīrì/xīngqītiān* = Sunday)
- `今天` (*jīntiān* = Today)
- Sentence: "Today is Sunday" (`今天星期天`)

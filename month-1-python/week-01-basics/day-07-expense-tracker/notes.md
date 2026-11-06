# Day 7: Week 1 Capstone & Exam Review Notes

## Student Exam Performance & Mastery Review

---

## 1. Exam Score & Detailed Breakdown

### Question 1: String Multiplication (`input() * 2`)
- **Student Answer:** `2020`
- **Result:** **100% Correct!** `input()` returns a string, so `"20" * 2` performs string repetition resulting in `"2020"`.

### Question 2: `for ... else` Execution Rule
- **Student Answer:** *"else will always run after the loop"*
- **Result:** **Partial / Correction:**
  - In Python, the `else` block on a loop runs **ONLY if the loop completes without hitting a `break` statement**.
  - If a loop is interrupted by a `break`, the `else` block is completely skipped!

### Question 3: Mutable Default Arguments
- **Student Answer:** *"Because in python list are reference type when first created the list it use same ref so old value will be present there."*
- **Result:** **100% Correct!** Spot on explanation. In Python, default arguments are evaluated only once at function definition time.

### Question 4: $O(1)$ Lookup Collections
- **Student Answer:** `dict`
- **Result:** **100% Correct!** Both `dict` and `set` provide average $O(1)$ constant time lookups.

### Question 5: `try / except / else / finally` Flow
- **Student Answer:** *"else run after except thn finally"*
- **Result:** **Correction on `else`:**
  - `else` runs **ONLY if NO exception occurs** in the `try` block. If `except` runs, `else` is skipped!
  - `finally` **ALWAYS** runs regardless of whether an exception occurred or not.

---

## 2. Developer English: Mock Interview Question #1

### Interviewer Question:
> *"Can you walk me through how your Expense Tracker is architected? How do you store the data in memory, and how does saving to a file work?"*

### Student's Raw Draft:
> *"I have choose list of dict as it has O(1) notion and easy to look for data efficiantly because later it will help us filter our list. I have valided all input and types , so that user can't input nagative amount . I have used with open to read and write file so that if any error happend python can do the cleanup and close the file."*

### Polished Senior Version (For Tech Interviews):
> "I architected the application using an in-memory list of dictionaries, where each dictionary represents an expense item with title, amount, and category fields. This structure allowed me to easily filter and transform records using list comprehensions. For input integrity, I implemented explicit type-casting and raised `ValueError` exceptions for negative numbers. Finally, I utilized Python's `with open()` context manager for file persistence, ensuring file streams are safely flushed and closed even if unexpected runtime errors occur."

---

## 3. High-Value Vocabulary Learned
- **Context Manager:** Ensures deterministic resource cleanup (`with` statement).
- **Data Integrity:** Preventing invalid, corrupted, or negative values from entering application state.
- **Flushed & Closed:** Writing buffered data completely to disk before closing the file handle.


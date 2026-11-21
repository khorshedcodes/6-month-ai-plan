# Day 21: Month 1 Python Foundations Final Milestone Exam

## Objective: Full Month 1 Comprehensive Review & Certification
This exam tests the complete set of capabilities mastered in Month 1:
- **Week 1:** Data types, conditionals, loops, functions, lists, dicts, exceptions, file I/O
- **Week 2:** OOP, `@dataclass`, JSON persistence, generators (`yield`), `pytest` unit tests, REST APIs
- **Week 3:** Decorators, async/await, `argparse`, structured `logging`, `src/` layout, hash maps & two pointers

---

## 1. The 6-Question Closed-Book Comprehensive Technical Exam
Answer each question directly from memory without looking at code or using AI:

1. **(Core Python):** What is the difference between a `list` and a `tuple`? In what scenario would an engineer deliberately choose a `tuple` over a `list`?
2. **(Decorators & Scope):** How does a decorator work under the hood? Why must a decorator with arguments (like `@retry(max_attempts=3)`) have 3 nested function layers instead of 2?
3. **(Memory & Streams):** What is the fundamental operational difference between `return` and `yield`? Why are generators critical when streaming tokens from Large Language Models (LLMs)?
4. **(Concurrency):** In Python's `asyncio`, what happens if you accidentally call a blocking function like `time.sleep(5)` inside an `async def` function? How does `asyncio.gather()` achieve concurrency?
5. **(Architecture & Best Practices):** Why do professional production applications use the `logging` module with structured levels (`INFO`, `WARNING`, `ERROR`) instead of standard `print()` statements?
6. **(Algorithms & Big-O):** Explain why checking `if x in my_dict:` runs in $O(1)$ constant time, while checking `if x in my_list:` runs in $O(N)$ linear time.

---

## 2. Developer English Task: Mock Technical Interview Q3 (C1 Level)
Deliver your response in 4 to 6 professional C1 sentences to the following question:
> *"How do you ensure your Python backend code is reliable, maintainable, and production-ready before deploying it?"*
*(Think about: type hints, unit testing with pytest, structured logging, error handling with timeouts, and linting with ruff).*

---

## 3. Mandarin Chinese Task: Lesson 4 (Review & Comprehensive Check)
Translate the following 3 workplace sentences into Pinyin:
1. "Hello, I am an engineer."
2. "My name is Khorshed."
3. "What time is it now?" (Bonus: "It is 7 o'clock now.")

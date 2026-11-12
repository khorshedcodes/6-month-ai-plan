# Week 2 Comprehensive Study & Revision Guide (`WEEK_2_REVISION.md`)

> **Purpose:** A single-page, high-yield summary of everything you learned in Week 2. Review this before tackling the **Day 14 Milestone Exam & Capstone Project**.

---

## 1. Object-Oriented Programming (Day 8)
- **Class vs. Instance:** A `class` is the blueprint (e.g. `BankAccount`); an instance is the actual object created in memory (e.g. `my_account`).
- **`self` (Python's `this`):** Points to the specific instance of the object. Every instance method must take `self` as its first parameter.
- **The Missing `self` Crash:** Calling `obj.method()` translates to `Class.method(obj)`. If `def method():` has no `self`, Python throws:
  `TypeError: method() takes 0 positional arguments but 1 was given`.
- **`__str__`:** Controls what prints when you do `print(obj)` or format it in an f-string, replacing the raw memory address with a clean string.

```python
class Expense:
    def __init__(self, title: str, amount: float):
        self.title = title
        self.amount = amount

    def __str__(self) -> str:
        return f"{self.title}: ${self.amount:.2f}"
```

---

## 2. Type Hints, `@dataclass`, & Inheritance vs. Composition (Day 9)
- **Type Hints:** `name: str`, `count: int`, `items: list[str]`, `user_id: int | None`. (Note: standard Python does *not* throw runtime errors on type mismatch; hints are for IDEs and static analysis).
- **`@dataclass` Superpower:** Eliminates boilerplate! Automatically generates `__init__`, `__repr__`, and `__eq__`.
- **Inheritance ("is-a"):** A child class specializes a parent class (`class BugTask(Task):`).
- **Composition ("has-a"):** A class holds or manages collections of other objects (`class Project:` holding `self.tasks = []`). Senior engineers prefer composition over inheritance for flexibility.

```python
from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    is_completed: bool = False

@dataclass
class BugTask(Task):
    severity: str = "Low"  # inherits id, title, is_completed!
```

---

## 3. JSON Persistence, `pathlib.Path`, & Datetime (Day 10)
- **The JSON Quartet:**
  - `json.dumps()`: Python object $\rightarrow$ JSON **string** in memory.
  - `json.loads()`: JSON **string** $\rightarrow$ Python dictionary.
  - `json.dump()`: Python object $\rightarrow$ writes directly to a **file**.
  - `json.load()`: Reads directly from a **file** $\rightarrow$ Python dictionary.
- **`asdict(obj)`:** Converts a `@dataclass` into a pure Python dictionary ready for JSON serialization.
- **Object Rehydration (`**kwargs`):** To turn a loaded dictionary back into a real class instance:
  `tasks = [Task(**item) for item in raw_json_list]`.
- **`pathlib.Path` Safety:** Always anchor to `Path(__file__).parent / "data.json"` to avoid working-directory bugs across operating systems.
- **Exception:** Catch `json.JSONDecodeError` to handle corrupted files gracefully.

---

## 4. Iterators, Generators (`yield`), & Lambdas (Day 11)
- **Eager vs. Lazy Evaluation:**
  - `return`: Calculates everything upfront, constructs the full list in RAM (eager).
  - `yield`: Produces **one item at a time**, pauses execution, and consumes $O(1)$ constant memory (lazy).
- **Why Generators Matter for AI:** Prevents `OutOfMemoryError` (OOM) when reading massive datasets or streaming real-time LLM token responses.
- **Lambdas:** Quick anonymous functions: `lambda x: x["latency"]`.
- **Custom Sorting:** `sorted(items, key=lambda x: x["latency"], reverse=True)`.
  *(Remember: always cast numerical strings to `int` before sorting, otherwise `"9ms"` is sorted after `"100ms"`!).*

---

## 5. Automated Unit Testing with `pytest` (Day 12)
- **Discovery Convention:** Pytest automatically discovers files named `test_*.py` and functions named `def test_*()`.
- **Plain `assert`:** No bloated matcher libraries needed; just `assert actual == expected`.
- **Testing Expected Exceptions:**
  ```python
  with pytest.raises(ValueError):
      account.withdraw(500.0)  # Must raise ValueError, otherwise test FAILS!
  ```
- **Fixtures (`@pytest.fixture`):** Supplies clean, isolated, reusable setup data for tests (DRY principle).

---

## 6. HTTP Requests & REST APIs (Day 13)
- **HTTP Status Codes:**
  - `2xx`: Success (`200 OK`, `201 Created`).
  - `4xx`: Client Error (`400 Bad Request`, `401 Unauthorized`, `404 Not Found`, `429 Rate Limit`).
  - `5xx`: Server Error (`500 Internal Server Error`, `502 Bad Gateway`).
- **`response.json()`:** Deserializes raw HTTP JSON bytes into a Python dictionary.
- **Defensive Networking:**
  - **Always set a timeout:** `requests.get(url, timeout=5)`.
  - **Always catch network drops:** `except requests.exceptions.RequestException as e:`.

---

## 7. Developer English Glossary to Review
| Technical Term | Everyday Meaning | Example in an Interview |
| :--- | :--- | :--- |
| **Encapsulation** | Keeping data and methods together in a class | *"I used classes to encapsulate task data and validation logic."* |
| **Serialization** | Converting memory objects into JSON / bytes | *"I serialized the dataclasses into JSON using `asdict()`."* |
| **Deserialization** | Rebuilding objects from JSON / bytes | *"I deserialized the JSON file back into `Task` instances using unpacking."* |
| **Lazy Evaluation** | Computing data only when requested | *"Generators use lazy evaluation with `yield` to keep memory footprint at $O(1)$."* |
| **Test Isolation** | Ensuring tests don't pollute each other | *"Fixtures guarantee test isolation by providing a fresh instance for every test."* |
| **Client vs. Server Error**| 4xx (caller's fault) vs. 5xx (host's fault) | *"404 indicates a client error, whereas 502 indicates a gateway failure."* |


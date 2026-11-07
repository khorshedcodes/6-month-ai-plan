# Day 8: Notes & Developer English Practice

## Topic: Object-Oriented Programming (Classes, Methods, `self`, `__str__`) & PR Descriptions

---

## 1. Key OOP Concepts & Gotchas Mastered

### The Nature of `self`
- `self` refers to the **specific instance of the class** (the created object), NOT the class definition itself.
- Unlike JavaScript where `this` is implicitly available, Python requires `self` to be declared explicitly as the first parameter of every instance method.

### The Missing `self` Gotcha (Important Python Error)
```python
class Car:
    def honk():
        print("Beep!")

c = Car()
c.honk()
```
- **Error Raised:** `TypeError: Car.honk() takes 0 positional arguments but 1 was given`.
- **Why?** When you call `c.honk()`, Python automatically passes `c` as the first argument (`Car.honk(c)`). Because `honk()` has zero parameters defined, it crashes!

### The Role of `__str__`
- Standard `print(obj)` outputs `<__main__.Expense object at 0x0000018...>` (the memory address).
- Implementing `__str__(self)` defines the human-readable string representation of the object when passed to `print()` or formatted in f-strings.

---

## 2. Professional Developer English: Pull Request (PR) Description

### Student's Raw Draft:
> **PR Title:** refector: migrate procedural expense tracker to OOP summary of Changes.  
> - Expense and ExpenseManager two class are created  
> - Expense present a expense and ExpenseManager act a center management by holding all the methods  

### Polished Version (For GitHub Pull Requests):
```markdown
### PR Title: refactor(expenses): migrate procedural dictionaries to OOP architecture

#### Summary of Changes:
- Introduced `Expense` domain model to encapsulate individual expense attributes (`title`, `amount`, `category`) and enforce validation rules.
- Created `ExpenseManager` class to manage the collection of expenses, providing clean methods for aggregation (`get_total`), filtering (`filter_by_category`), and reporting (`list_all`).
- Implemented `__str__` dunder method on `Expense` for clear string representation.

#### Why This Refactor Was Needed:
- Replaced loose, untyped dictionary structures with structured objects, preventing key typos and runtime `KeyError` crashes.
- Centralized business logic inside dedicated classes rather than relying on global lists and scattered functions.

#### How to Test:
1. Run `python month-1-python/week-02-oop-and-files/day-08/code.py`.
2. Verify that expenses are added, listed cleanly without memory address artifacts, and total sums compute accurately.
```

---

## 3. High-Value Tech Vocabulary Learned
- **Encapsulation:** Bundling data and the methods that operate on that data inside a single unit (class).
- **Instance vs. Class:** The class is the blueprint (e.g. `Car`); the instance is the actual object created in memory (e.g. `my_car`).
- **Domain Model:** A representation of a real-world concept in code (e.g. `Expense`).
- **Dunder Method:** Double-underscore methods in Python (`__init__`, `__str__`) that integrate with Python's language features.


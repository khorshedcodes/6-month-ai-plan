# Day 8: Object-Oriented Programming (Classes, __init__, self, methods, __str__)

## Learning Objectives
1. Understand Classes as blueprints vs. Objects as instances.
2. The `__init__` constructor method and `self` (comparison to JS `this`).
3. Instance attributes vs. methods.
4. The `__str__` dunder method for clean string representations.
5. Why OOP helps scale applications beyond loose dictionaries and global state.

---

## Daily Task: Refactoring Expense Tracker into OOP (Without AI)
Build two classes:
1. `Expense`:
   - Attributes: `title`, `amount`, `category`.
   - Method `__str__`: returns clean formatted string (`"Title: ... | Amount: $... | Category: ..."`).
2. `ExpenseManager`:
   - Attribute: `self.expenses` (list holding `Expense` objects).
   - Methods:
     - `add_expense(expense: Expense)`: appends object.
     - `get_total()`: calculates and returns sum of all expense amounts.
     - `filter_by_category(category)`: returns a filtered list of `Expense` objects.
     - `list_all()`: prints all expenses using their `__str__` format.

---

## Developer English Task: Writing a Pull Request (PR) Description
Write a professional PR description summarizing the transition from procedural dictionary code to Object-Oriented architecture:
- **Summary of Changes**
- **Why this refactor was needed**
- **How to test**


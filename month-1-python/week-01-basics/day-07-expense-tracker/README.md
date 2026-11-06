# Day 7: Week 1 Capstone & Closed-Book Examination

## Project Objective: CLI Personal Expense Tracker
Build a standalone, menu-driven CLI program from scratch that combines everything learned in Week 1:
- Variables & Type Casting (Day 1)
- Loops & Conditionals (Day 2)
- Modular Functions & Docstrings (Day 3)
- Lists & Dictionaries for Data Storage (Day 4)
- File Persistence with `with open()` (Day 5)
- Defensive Error Handling (`try/except`) (Day 6)

---

## Technical Specifications

### Data Structure:
An in-memory list of dictionaries:
```python
expenses = [
    {"title": "Groceries", "amount": 45.50, "category": "Food"},
    {"title": "Bus pass", "amount": 20.00, "category": "Transport"}
]
```

### Menu Options:
1. **Add Expense:** Prompt for title, amount (float, must be > 0), and category.
2. **List All Expenses:** Print each item formatted cleanly with an index, and display the **total sum** of all expenses.
3. **Filter by Category:** Ask user for category (e.g. "Food"), print matching expenses and subtotal.
4. **Save Expenses to File:** Save current expenses to `expenses.txt` (format: `title,amount,category` per line).
5. **Load Expenses from File:** Read from `expenses.txt` and populate the list (must handle `FileNotFoundError` without crashing).
6. **Exit:** Print goodbye and terminate.

---

## Rules
- **No AI generation** — write this independently.
- Clean functions for each action (`add_expense`, `list_expenses`, `save_to_file`, `load_from_file`, etc.).


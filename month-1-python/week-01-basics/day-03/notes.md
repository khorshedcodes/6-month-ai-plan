# Day 3: Notes & Developer English Practice

## Topic: Functions, Scope, and Google-Style Docstrings

---

## 1. Key Concept & Traps Mastered

### The Mutable Default Argument Trap (Crucial Python Gotcha)
In Python, default arguments are evaluated **only once** when the function is defined, NOT each time the function is called.
```python
# DANGEROUS:
def add_item(val, items=[]):
    items.append(val)
    return items

# First call: returns [1]
# Second call: returns [1, 2] (re-uses the SAME list in memory!)

# IDIOMATIC FIX:
def add_item(val, items=None):
    if items is None:
        items = []
    items.append(val)
    return items
```

### Python's `None` vs JavaScript `null`
- JavaScript has both `null` and `undefined`.
- Python has a single singleton object: `None` (capital N, `<class 'NoneType'>`).
- If a function finishes without an explicit `return` statement, Python returns `None`.

---

## 2. Professional Docstrings Practice

### Google-Style Docstring Format:
```python
def evaluate_password(password: str) -> str:
    """Evaluates the strength of a given password based on length, digits, and casing.

    Args:
        password (str): The raw password string to evaluate.

    Returns:
        str: The password rating ('Weak', 'Medium', or 'Strong').
    """
```

---

## 3. Useful Tech Vocabulary
- **Positional Arguments:** Arguments passed based on order/position.
- **Keyword Arguments:** Arguments explicitly mapped to parameter names (`param=value`).
- **Default Argument:** A parameter value used when the caller does not supply one.
- **Mutable:** An object that can be altered after creation (e.g., `list`, `dict`).
- **Docstring:** In-code documentation string accessible via `__doc__` or IDE tooltips.


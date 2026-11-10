# Day 12: Automated Unit Testing with pytest

## Learning Objectives
1. Why automated testing matters in professional development.
2. The core testing tool: `pytest` and simple `assert` statements.
3. Test file and function naming conventions (`test_*.py` and `def test_*()`).
4. Testing edge cases and expected exceptions (`with pytest.raises(...)`).
5. Reusable test setup with `pytest.fixture`.

---

## Daily Task: Production Unit Test Suite (Without AI)
We will take your Week 1 & 2 logic and write a real automated test suite:
1. `bank_account.py`:
   - A class `BankAccount(initial_balance: float = 0.0)`
   - Methods:
     - `deposit(amount: float) -> float` (raises `ValueError` if amount <= 0)
     - `withdraw(amount: float) -> float` (raises `ValueError` if amount <= 0 or amount > balance)
     - `get_balance() -> float`
2. `test_bank_account.py`:
   - Write 6 comprehensive unit tests:
     - Test initial balance (default and custom)
     - Test successful deposit
     - Test deposit with invalid amount (must raise `ValueError`)
     - Test successful withdrawal
     - Test withdrawal with insufficient funds (must raise `ValueError`)
     - Use a `@pytest.fixture` to provide a pre-funded test account!

---

## Developer English Task: Test Case Specifications
Write a test plan in clean English explaining the test scenarios, expected outputs, and edge cases.


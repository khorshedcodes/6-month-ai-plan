# Day 12: Notes & Developer English Practice

## Topic: Automated Unit Testing with Pytest & Test Specifications

---

## 1. Key Concepts & Architecture Mastered

### Pytest Discovery Conventions
- **Test Files:** Any file matching `test_*.py` or `*_test.py`.
- **Test Functions:** Any function starting with `test_*()`.
- **Test Classes:** Any class starting with `Test*` (without `__init__`).

### Testing Exceptions: `with pytest.raises(...)` vs. `try / except`
- Using `try / except` in a test is error-prone: if the code fails to raise an error, the `except` block never executes, and the test mistakenly passes!
- `with pytest.raises(ExpectedException):` asserts that an exception MUST be thrown; if no exception is raised, pytest fails the test immediately.

### Reusable Setup with `@pytest.fixture`
- Eliminates repeated boilerplate across test cases (DRY principle).
- Guarantees **test isolation**: each test gets a freshly instantiated fixture object, preventing state leakage between tests.

---

## 2. Professional Developer English: Test Specification Summary

### Student's Raw Draft:
> *"In this test I have successfully implemented the case withdraw , deposit and get blance . I have tested with the nagative vlaue and over widrawn to raise errors and findout everything going smothly . fixture in pytest let us reduce repeted code and easily get a initial value to test our test cases."*

### Polished Version (For Code Reviews & Test Documentation):
> "I implemented an automated test suite covering the core banking operations: deposits, withdrawals, and balance inquiries. In addition to verifying standard happy paths, I tested critical edge cases—including negative initial balances and overdraft attempts—to ensure expected `ValueError` exceptions are raised deterministically. Finally, I utilized a `@pytest.fixture` to supply a pre-funded test account, reducing code duplication and guaranteeing complete test isolation."

---

## 3. High-Value Tech Vocabulary Learned
- **Happy Path:** The default execution path where inputs are valid and no errors occur.
- **Edge Case:** Boundary conditions or invalid inputs that could trigger failures (e.g. negative numbers, zero balance, overdrafts).
- **Test Isolation:** Ensuring the outcome of one test cannot affect the state or result of another test.
- **Fixture:** A helper that provides a consistent, reproducible baseline environment or data for tests.
- **Deterministic:** An operation or test that produces the exact same result every single time it runs.


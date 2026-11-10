# Day 12: Automated Test Suite with Pytest
# Write your test functions and fixtures here independently.
import pytest
from bank_account import BankAccount

# Example structure:
# def test_initial_balance():
#     account = BankAccount(100.0)
#     assert account.get_balance() == 100.0
def test_default_balance():
    account = BankAccount()
    assert account.get_balance() == 0.0

def test_custom_initial_balence():
    account = BankAccount(250.0)
    assert account.get_balance() == 250.0

def test_initial_negative_balance_raises_error():
    with pytest.raises(ValueError):
        a = BankAccount(-20.0)

@pytest.fixture
def account():
    return BankAccount(100.0)

def test_deposit_increases_balance(account):
     account.deposit(50.0)
     assert account.get_balance() == 150.0

def test_withdraw_insufficient_funds_raises_error(account):
    with pytest.raises(ValueError):
        account.withdraw(200.00)
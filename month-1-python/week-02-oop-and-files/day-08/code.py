# Day 8: Code Implementation
# Object-Oriented Refactoring of Expense Tracker
# Write your classes and main flow here independently.

class Expense :
    def __init__(self,title,amount,category):
        self.title = title
        if amount < 0 :
            raise ValueError("Amount cannot be negative.")
        self.amount = amount
        self.category = category

    def __str__(self):
        return f"Title: {self.title} | Amount: {self.amount:.2f} | Category: {self.category}"


class ExpenseManager:
    def __init__(self):
        self.expenses = []
    def add_expense(self,expense):
        self.expenses.append(expense)
    def get_total(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        return total
    def filter_by_category(self,category):
        new_list = [expense for expense in self.expenses if expense.category==category]
        return new_list
    
    def list_all(self):
        if not self.expenses:
           return print("No expenses recorded.")
        for expense in self.expenses:
            expense.__str__()



m1 = ExpenseManager()
e1 = Expense(title="Milk", amount=200.40, category="grocery")
e2 = Expense(title="Rice buy", amount=100.00, category="grocery")
e3 = Expense(title="burger", amount=20.0, category="food")

m1.add_expense(e1)
m1.add_expense(e2)
m1.add_expense(e3)

print("--- All Expenses ---")
m1.list_all()

print(f"\nTotal: ${m1.get_total():.2f}")

print("\n--- Groceries Only ---")
groceries = m1.filter_by_category("grocery")
for item in groceries:
    print(item)
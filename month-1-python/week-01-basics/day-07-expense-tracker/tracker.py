# Day 7: Week 1 Capstone Project
# CLI Expense Tracker
# Write your complete implementation here independently.


should_run = True
expenses = []

def show_menu():
    print("=== Personal Expense Tracker ===")
    print("1. Add Expense ")
    print("2. List All Expenses ")
    print("3. Filter Category")
    print("4. Save File")
    print("5. Load from File")
    print("6. Exit")

def add_expense():
    title = input("Enter expense title: ")
    amount = float(input("Please enter the amount: "))
    if amount < 0:
        raise ValueError("Amount must be greater then zero.")
    category = input("Enter category name: ")

    exp = {"title": title,"amount":amount,"category":category}
    expenses.append(exp)

def show_expense():
    if not expenses:
        print("There is no expenses to show.")
    total = 0
    for exp in expenses:
        total += exp['amount']
        print(f"title - {exp['title']}, amount - {exp["amount"]}, category - {exp["category"]}")
    if len(expenses) != 0 :
        print(f"Total Amount: {total:.2f}")
    

def filter_expense():
    desire_cat = input("Enter category to filter: ")
    filterd_cat = [exp for exp in expenses if exp["category"] == desire_cat]
    if len(filterd_cat) == 0 :
        print("No expense found in this category.")
    total = 0
    for exp in filterd_cat:
         total += exp['amount']
         print(f"title - {exp["title"]}, amount - {exp["amount"]}, category - {exp["category"]}")
     
    print(f"Subtotal Amount: {total:.2f}")

def save_file():
    with open("expenses.txt","w") as file:
        for ind,exp in enumerate(expenses, start=1):
            file.write(f"{ind}. Title - {exp["title"]} | Amount - {exp["amount"]} | Category - {exp["category"]}")

def read_file():
    try:
        with open("expenses.txt","r") as file:
            for line in file:
                clean_line = line.strip()
                line_without_index = clean_line.split(".")[1]
                print(line_without_index)
    except FileNotFoundError as e:
        print(f"Error : {e}")

def main():
    while(should_run):
        show_menu()
        user_input = int(input("Select your menu item: "))
        if user_input <= 0 or user_input > 6 :
            print("Please Select a valid manu option")
            continue
        if user_input == 1:
            add_expense()
        elif user_input == 2:
            show_expense()
        elif user_input == 3:
            filter_expense()
        elif user_input == 4:
            save_file()
        elif user_input == 5:
            read_file()
        elif user_input == 6:
             should_run = False
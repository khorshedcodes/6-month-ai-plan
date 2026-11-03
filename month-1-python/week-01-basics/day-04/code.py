# Day 4: Code Implementation
# In-Memory Contact Book (CRUD)
# Write your implementation here independently.
contacts = {}
should_run = True

def print_menu():
    print("=== Contact Book ====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. List All Contact")
    print("6. Exit")

def add_contact():
    contact_name = input("Enter name: ")
    contact_number = input ("Enter number: ")
    contacts[contact_name] = contact_number
    return

def search_contact():
    contact_name = input("Enter name: ")
    print(contacts.get(contact_name,"Contact not found."))

def update_contact():
    contact_name = input("Enter name: ")
    if contacts.get(contact_name):
        new_number = input("Enter new number: ")
        contacts[contact_name] = new_number
    else:
        print("Not found")

def delete_contact():
    contact_name = input("Enter name: ")
    if contacts.get(contact_name):
        del contacts[contact_name]
    


while(should_run):
    print_menu()
    user_pick = int(input("Please enter your choice: "))
    if(user_pick > 6 or user_pick <=0):
        print("Please Choose between 1 to 6!")
        continue
    if user_pick == 1 :
        add_contact()
    elif user_pick == 2:
        search_contact()
    elif user_pick == 3:
        update_contact()
    elif user_pick == 4:
        delete_contact()
    elif user_pick == 5:
        if len(contacts) == 0:
            print("No contacts Saved")
        else:
            for name,contact in contacts.items():
                print(f"{name} - {contact}")
    elif user_pick == 6:
        print("Goodbye!")
        should_run = False


        
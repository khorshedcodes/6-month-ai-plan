# Day 3: Code Implementation
# Write your code here independently.

def check_length(password,min_length=8):
    return len(password) >= min_length

def has_digit(password):
    count = 0
    for c in password:
        if c.isdigit():
            count += 1
    return count > 0

def has_uppercase(password):
    count = 0
    for c in password:
        if c.isupper():
            count += 1
    return count > 0

def evaluate_password(password):
    currect_length = check_length(password)
    with_degit = has_digit(password)
    with_uppercase = has_uppercase(password)

    if currect_length and with_degit and with_uppercase:
        return "Strong"
    elif(currect_length and with_degit) or (currect_length and with_uppercase):
        return "Medium"
    else:
        return "Weak"


def Main():
    userpass = input("Enter your password: ")
    result = evaluate_password(userpass)
    print(f"Your password is {result}")


Main()
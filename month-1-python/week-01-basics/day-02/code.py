# Day 2: Code Implementation
# Write your code here independently.
import random

secret = random.randint(1,50)

for i in range(1,6):
    guess_number = int(input("Guess the number: "))
    if guess_number > secret:
        print("Too high! Try again.")
    elif guess_number < secret:
        print("Too low! Try again.")
    else:
        print(f"Congratulations! You got it in {i} attemps!")
        break
else:
    print(f"Game over! The number was {secret}")
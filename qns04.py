# ✨ Question 4  
# Write a program that simulates 
# a **Guessing Game**:  
# Pick a secret number, and
# keep asking the user to guess until they get it right.

# using random module to generate a secret number
import random
secret_number = random.randint(1, 100)  # Random number between 1 and 100
guess = None
while guess != secret_number:
    guess = int(input("Guess the secret number (between 1 and 100): "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the secret number:", secret_number)
        
# or using a predefined secret number

secret_number = 42
guess = None
while guess != secret_number:
    guess = int(input("Guess the secret number (between 1 and 100): "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the secret number:", secret_number)
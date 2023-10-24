# Day 08
# Guess the Number in Python

import random

# Generate a random number between 1 and 5
num = random.randint(1, 5)
guess = None

# Keep prompting the user to guess the number until they guess correctly
while guess != num:
    # Allowing the user to input their guess as an integer
    guess = int(input("Guess a number between 1 and 5: "))
    
    # Check if the guessed number matches the generated random number
    if guess == num:
        print("Congratulations! You won :)")  # Print a success message if the guess is correct
        break                                                     # Exit the loop if the guess is correct
    else:
        print("Try Again :(")  # Print a message to try again if the guess is incorrect


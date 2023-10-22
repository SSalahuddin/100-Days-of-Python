# Day 06
# 🔐Improved Password Generator in Python 💡

import random
import string

# Define a function to generate a random password of a specified length.
def generate_password(length):
    # Define the character set for the password, including letters, digits, and punctuation.
    chars = string.ascii_letters + string.digits + string.punctuation

    # Generate the password by joining random characters from the character set.
    password = ''.join(random.choice(chars) for _ in range(length))

    # Return the generated password.
    return password

# Prompt the user to enter the desired password length as an integer.
length = int(input("Enter password length: "))

# Initialize an empty string to store the generated password.
password = ""

# Check if the password length is less than 8 characters.
if length < 8:
    # If the length is insufficient, inform the user.
    print("Password length should be at least 8 characters.")
else:
    # If the length is adequate, generate a password using the 'generate_password' function.
    password = generate_password(length)
    
    # Display the generated password to the user.
    print("Generated Password:", password)

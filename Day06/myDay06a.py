# Day 06
# 🔐Crafting a Simple Password Generator in Python 💡

# Import the 'random' module to generate random characters.
import random

# Define the set of characters that can be used to generate the password.
chars = "abcdefghijlkmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(){}|:<>?/"

# Prompt the user to enter the desired length of the password.
length = int(input("Enter length: "))

# Initialize an empty string to store the generated password.
password = ""

# Loop 'length' times to build the password character by character.
for a in range(length):
    # Choose a random character from the 'chars' set and add it to the password.
    password += random.choice(chars)

# Print the generated password.
print(password)



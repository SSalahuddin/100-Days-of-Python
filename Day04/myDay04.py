# Day 04
# Dice Roller Simulation using Decision Making and Dictionary in Python
import random

dice_patterns = {	# Create a dictionary to store dice face patterns
    1: "[-----]\n[         ]\n[    0   ]\n[         ]\n[-----]",
    2: "[-----]\n[0       ]\n[         ]\n[       0]\n[-----]",
    3: "[-----]\n[0       ]\n[    0   ]\n[       0]\n[-----]",
    4: "[-----]\n[0     0]\n[         ]\n[0     0]\n[-----]",
    5: "[-----]\n[0     0]\n[    0   ]\n[0     0]\n[-----]",
    6: "[-----]\n[0     0]\n[0     0]\n[0     0]\n[-----]"
}
num = random.randint(1, 6)  # generate a random number between 1 and 6
print("The number rolled is:", num)

# Check if the number is in the dictionary and print the corresponding pattern
if num in dice_patterns:
    print(dice_patterns[num])
else:
    print("Invalid option")


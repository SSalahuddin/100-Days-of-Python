# Day 10
# Multiple-Choice Quiz Game in Python

import random

# Define a list of questions, options, and correct answers as a dictionary
quiz_data = [
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["a) Venus", "b) Mercury", "c) Earth", "d) Mars"],
        "correct_answer": "d"
    },
    {
        "question": "Who developed the theory of relativity?",
        "options": ["a) Isaac Newton", "b) Albert Einstein", "c) Galileo Galilei", "d) Marie Curie"],
        "correct_answer": "b"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["a) Pacific Ocean", "b) Indian Ocean", "c) Southern Ocean", "d) Atlantic Ocean"],
        "correct_answer": "a"
    },
    {
        "question": "What is the fastest land animal on Earth?",
        "options": ["a) Cheetah", "b) Lion", "c) Elephant", "d) Giraffe"],
        "correct_answer": "a"
    },
    {
        "question": "Who is the author of the Harry Potter book series?",
        "options": ["a) J.R.R. Tolkien", "b) C.S. Lewis", "c) J.K. Rowling", "d) George R.R. Martin"],
        "correct_answer": "c"
    }
]

# Create a list of indices from 0 to the length of quiz_data - 1
indices = list(range(len(quiz_data)))

# Shuffle the indices to get a random order
random.shuffle(indices)

# Initialize a variable to keep track of the score
score = 0

# Iterate through the questions and ask the user
for i in indices:
    current_question = quiz_data[i]
    
    print(f"Question: {current_question['question']}")
    for option in current_question['options']:
        print(option)
    
    user_answer = input("Your answer (a/b/c/d): ").strip().lower()
    
    # Check if the user's answer is correct
    if user_answer == current_question['correct_answer']:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {current_question['correct_answer'].upper()}\n")

# Display the final score
print(f"You scored {score} out of {len(quiz_data)} questions.")

if score == len(quiz_data):
    print("Congratulations! You are the quiz champion!")

# Day 05
# 🧠 Quiz Master - Test Your Knowledge with Python!

import random

# Define a list of questions and answers as tuples (question, answer)
qa_pairs = [ ("What is 2 + 2?", "4"),
                      ("What is 10 * 5?", "50"),
                      ("What is 15 - 7?", "8"),
                      ("What is 30 / 3?", "10"),
                      ("What is 2 ** 3?", "8") ]

# Shuffle the question-answer pairs to get a random order
random.shuffle(qa_pairs)

# Initialize a variable to keep track of the score
score = 0

# Iterate through the questions and ask the user
for question, answer in qa_pairs:
    print(f"Question: {question}")
    user_answer = input("Your answer: ").strip()
    
    # Check if the user's answer is correct
    if user_answer.lower() == answer.lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {answer}\n")

# Display the final score and congratulate the winner
print(f"You scored {score} out of {len(qa_pairs)} questions.")
if score == len(qa_pairs):
    print("Congratulations! You are the quiz champion!")
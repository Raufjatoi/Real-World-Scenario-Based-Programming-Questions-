# 8. Simple Quiz with Timer: Create a program for a timed quiz. It should display a set of questions
# with multiple-choice answers and a timer for each question. Users should select their answers
# within the time limit. The program should calculate the score and display the results upon
# completion.
import time

# Define questions, choices, and correct answers
questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "What is the chemical symbol for water?",
]
choices = [
    ["A. London", "B. Paris", "C. Berlin"],
    ["A. Venus", "B. Mars", "C. Jupiter"],
    ["A. H2O", "B. CO2", "C. O2"],
]
correct_answers = ["B", "B", "A"]

# Function to display questions and choices
def display_question(question_num):
    print(f"Question {question_num + 1}: {questions[question_num]}")
    for choice in choices[question_num]:
        print(choice)
    print()

# Function to check answer and calculate score
def check_answer(question_num, answer):
    if answer.upper() == correct_answers[question_num]:
        return 1
    return 0

# Main function for the quiz
def quiz():
    score = 0
    num_questions = len(questions)
    time_per_question = 10  # Time per question in seconds

    print("Welcome to the Quiz!\n")
    for i in range(num_questions):
        display_question(i)
        start_time = time.time()
        while True:
            remaining_time = int(time_per_question - (time.time() - start_time))
            if remaining_time <= 0:
                print("Time's up!")
                break
            answer = input(f"Time left: {remaining_time} seconds. Enter your answer: ")
            if answer.upper() in ["A", "B", "C"]:
                score += check_answer(i, answer)
                break
            else:
                print("Invalid input. Please enter A, B, or C.")

    print("\nQuiz completed!")
    print(f"Your score: {score}/{num_questions}")

# Run the quiz
quiz()


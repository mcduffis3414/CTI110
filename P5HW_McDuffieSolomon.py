# Math Quiz
# CTI-110
# Solomon McDuffie
# 3 May 2023

import random

def generate_numbers():
    """Generates two random numbers between 1 and 100."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def get_user_answer():
    """Gets the user's answer to the math question."""
    user_answer = input("Enter your answer: ")
    while not user_answer.isdigit():
        user_answer = input("Invalid input. Please enter a valid integer: ")
    return int(user_answer)

def play_addition_quiz():
    """Plays the addition quiz game."""
    num_guesses = 0
    num1, num2 = generate_numbers()
    answer = num1 + num2
    print(f"What is {num1} + {num2}?")

    while True:
        user_answer = get_user_answer()
        num_guesses += 1
        if user_answer == answer:
            print(f"Congratulations! You got the correct answer on guess #{num_guesses}.")
            break
        elif user_answer < answer:
            print("Too low. Guess again.")
        else:
            print("Too high. Guess again.")

def play_subtraction_quiz():
    """Plays the subtraction quiz game."""
    num_guesses = 0
    num1, num2 = generate_numbers()
    answer = num1 - num2
    print(f"What is {num1} - {num2}?")

    while True:
        user_answer = get_user_answer()
        num_guesses += 1
        if user_answer == answer:
            print(f"Congratulations! You got the correct answer on guess #{num_guesses}.")
            break
        elif user_answer < answer:
            print("Too low. Guess again.")
        else:
            print("Too high. Guess again.")

def show_menu():
    """Displays the menu of options."""
    print("MAIN MENU")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")

def get_user_choice():
    """Gets the user's choice of quiz to play."""
    user_choice = input("Enter your choice: ")
    # Check if the input is a valid integer
    while not user_choice.isdigit():
        user_choice = input("Invalid input. Please enter a valid integer: ")
    return int(user_choice)

if __name__ == "__main__":
    while True:
        show_menu()
        user_choice = get_user_choice()
        if user_choice == 1:
            play_addition_quiz()
        elif user_choice == 2:
            play_subtraction_quiz()
        elif user_choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


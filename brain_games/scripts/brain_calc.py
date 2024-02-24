#!/usr/bin/env python3
import random
import prompt


def main():
    NUMBER_OF_PLAYS = 3

    print("Welcome to the Brain Games!")
    player_name = prompt.string("May I have your name? ")
    print(f"Hello, {player_name}!")

    print("What is the result of the expression?")

    for i in range(NUMBER_OF_PLAYS):
        OPERATIONS = ("+", "-", "*")
        
        question_number_1 = random.randint(1, 100)
        question_number_2 = random.randint(1, 100)
        question_operation = random.choice(OPERATIONS)
        right_answer = eval(f"{question_number_1}{question_operation}{question_number_2}")
        
        print(f"Question: {question_number_1} {question_operation} {question_number_2}")
        
        player_answer = prompt.string("Your answer: ")

        if player_answer == str(right_answer):
            print("Correct!")
        else:
            print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {player_name}!")
            return

    print(f"Congratulations, {player_name}!")
    return


if __name__ == "__main__":
    main()

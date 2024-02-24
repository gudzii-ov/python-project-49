#!/usr/bin/env python3
import random
import prompt


def main():
    NUMBER_OF_PLAYS = 3

    print("Welcome to the Brain Games!")
    player_name = prompt.string("May I have your name? ")
    print(f"Hello, {player_name}!")

    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")

    for i in range(NUMBER_OF_PLAYS):
        question_number = random.randint(1, 100)
        print(f"Question: {question_number}")
        player_answer = prompt.string("Your answer: ")
        right_answer = "yes" if question_number % 2 == 0 else "no"
        if player_answer == right_answer:
            print("Correct!")
        else:
            print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {player_name}!")
            return

    print(f"Congratulations, {player_name}!")
    return


if __name__ == "__main__":
    main()

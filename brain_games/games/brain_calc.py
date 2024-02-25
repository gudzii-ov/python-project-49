import random
import brain_games.game_engine


message = "What is the result of the expression? version 6"


def get_question_and_answer():
    OPERATIONS = ("+", "-", "*")

    question_number_1 = random.randint(1, 100)
    question_number_2 = random.randint(1, 100)
    question_operation = random.choice(OPERATIONS)

    question = f"{question_number_1} {question_operation} {question_number_2}"

    right_answer = str(eval(question))

    return (question, right_answer)


def play_brain_calc():
    brain_games.game_engine.play_game(message, get_question_and_answer)

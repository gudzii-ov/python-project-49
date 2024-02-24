import random
import brain_games.game_engine


game_message = "What is the result of the expression? version 6"


def get_question_and_answer():
    OPERATIONS = ("+", "-", "*")

    question_number_1 = random.randint(1, 100)
    question_number_2 = random.randint(1, 100)
    question_operation = random.choice(OPERATIONS)
    game_question = f"{question_number_1} {question_operation} {question_number_2}"
    right_answer = str(eval(game_question))

    return (game_question, right_answer)


def play_brain_calc():
    brain_games.game_engine.play_game(game_message, get_question_and_answer)

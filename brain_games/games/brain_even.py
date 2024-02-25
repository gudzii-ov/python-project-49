import random
import brain_games.game_engine


message = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def get_question_and_answer():
    question_number = random.randint(1, 100)
    right_answer = "yes" if question_number % 2 == 0 else "no"

    return (question_number, right_answer)


def play_brain_even():
    brain_games.game_engine.play_game(message, get_question_and_answer)
    return

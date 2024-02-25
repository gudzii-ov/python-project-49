import random
import brain_games.game_engine


message = "Find the greatest common divisor of given numbers."


def get_gcd(number1, number2):
    return number1 if number2 == 0 else get_gcd(number2, number1 % number2)


def get_question_and_answer():
    question_number_1 = random.randint(1, 100)
    question_number_2 = random.randint(1, 100)
    game_question = f"{question_number_1} {question_number_2}"
    right_answer = str(get_gcd(question_number_1, question_number_2))

    return (game_question, right_answer)


def play_brain_gcd():
    brain_games.game_engine.play_game(message, get_question_and_answer)
    return

import random
import math
import brain_games.game_engine


game_message = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def is_prime(number):
    number_square = math.sqrt(number)

    def iter(divisor):
        if divisor > number_square:
            return True
        elif number % divisor == 0:
            return False
        else:
            return iter(divisor + 1)

    return iter(2)


def get_question_and_answer():
    question_number = random.randint(2, 100)

    right_answer = "yes" if is_prime(question_number) else "no"

    return (question_number, right_answer)


def play_brain_prime():
    brain_games.game_engine.play_game(game_message, get_question_and_answer)
    return

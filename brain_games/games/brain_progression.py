import random
import brain_games.game_engine


message = "What number is missing in the progression?"


def generate_progression(length):
    progression = []

    first_number = random.randint(1, 20)
    progression_step = random.randint(2, 5)

    for i in range(length):
        progression.append(first_number + i * progression_step)

    return progression


def get_question_and_answer():
    progression_length = random.randint(5, 10)
    progression = generate_progression(progression_length)

    hidden_number_index = random.randint(0, progression_length - 1)
    hidden_number = progression[hidden_number_index]

    progression[hidden_number_index] = ".."

    converted_progression = map(str, progression)

    game_question = " ".join(converted_progression)

    right_answer = str(hidden_number)

    return (game_question, right_answer)


def play_brain_progression():
    brain_games.game_engine.play_game(message, get_question_and_answer)
    return

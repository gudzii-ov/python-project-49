import prompt


def play_game(game_message, get_question_and_answer):
    ROUNDS_COUNT = 3

    print("Welcome to the Brain Games!")

    player_name = prompt.string("May I have your name? ")
    print(f"Hello, {player_name}!")

    print(game_message)

    for i in range(ROUNDS_COUNT):
        (game_question, game_answer) = get_question_and_answer()

        print(f"Question: {game_question}")
        player_answer = prompt.string("Your answer: ")

        if player_answer == game_answer:
            print("Correct!")
        else:
            print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{game_answer}'.")
            print(f"Let's try again, {player_name}!")
            return

    print(f"Congratulations, {player_name}!")
    return

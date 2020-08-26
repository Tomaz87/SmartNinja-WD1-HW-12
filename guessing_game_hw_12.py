import random
import json
import datetime


# Loop function for playing the game.
def play_game(level="easy"):
    player = input("Player name: ")
    secret = random.randint(1, 100)
    attempts = 0

    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())

    wrong_guesses = []

    while True:
        guess = int(input("Guess the secret number between 1 and 100: "))
        attempts += 1

        if guess == secret:
            score_list.append({"player": player,
                               "secret_number": secret,
                               "attempts": attempts,
                               "date": str(datetime.datetime.now()),
                               "wrong_guesses": wrong_guesses})
            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))
            print("You've guessed the secret number! It's number: " + str(secret) + " Good job! ;)")
            print("Attempts needed: " + str(attempts))
            break
        elif guess < secret and level == "easy":
            print("Try something bigger! :)")
        elif guess > secret and level == "easy":
            print("Try something smaller! :)")
        else:
            print("Your guess is incorrect. Try again ;)")

        wrong_guesses.append(guess)


# Get a list of all scores.
def get_all_scores():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


# Get a list of top 3 scores.
def get_top_scores():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        top_scores = sorted(score_list, key=lambda x: x["attempts"])[:3]
        return top_scores


while True:
    selection = input("Would you like to: \n"
                      "P) play a game, \n"
                      "A) see all scores, \n"
                      "T) see top 3 scores, \n"
                      "Q) quit the game: \n")

    if selection.upper() == "P":
        level = input("Choose your level (easy/hard): ")
        play_game(level=level)
    elif selection.upper() == "A":
        print("All scores:")
        for score_dict in get_all_scores():
            score_text = f"Player {score_dict.get('player')} guessed the secret no. {score_dict.get('secret_number')} in {score_dict.get('attempts')} attempts on {score_dict.get('date')}. {score_dict.get('player')} also tried with numbers {score_dict.get('wrong_guesses')}."
            print(score_text)
    elif selection.upper() == "T":
        print("Top scores:")
        for score_dict in get_top_scores():
            score_text = f"Player {score_dict.get('player')} guessed the secret no. {score_dict.get('secret_number')} in {score_dict.get('attempts')} attempts on {score_dict.get('date')}. {score_dict.get('player')} also tried with numbers {score_dict.get('wrong_guesses')}. "
            print(score_text)
    else:
        break

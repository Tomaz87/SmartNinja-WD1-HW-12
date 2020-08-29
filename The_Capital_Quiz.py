import random
import json
import datetime


# Dictionary of European countries and their capitals.
europe_capitals = {
    "Albania": "Tirana",
    "Andorra": "Andorra la Vella",
    "Armenia": "Yerevan",
    "Austria": "Vienna",
    "Azerbaijan": "Baku",
    "Belarus": "Minsk",
    "Belgium": "Brussels",
    "Bosnia and Herzegovina": "Sarajevo",
    "Bulgaria": "Sofia",
    "Croatia": "Zagreb",
    "Cyprus": "Nicosia",
    "Czech Republic": "Prague",
    "Denmark": "Copenhagen",
    "Estonia": "Tallinn",
    "Finland": "Helsinki",
    "France": "Paris",
    "Georgia": "Tbilisi",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Hungary": "Budapest",
    "Iceland": "Reykjavik",
    "Ireland": "Dublin",
    "Italy": "Rome",
    "Kazakhstan": "Nur Sultan",
    "Latvia": "Riga",
    "Liechtenstein": "Vaduz",
    "Lithuania": "Vilnius",
    "Luxembourg": "Luxembourg",
    "Malta": "Valletta",
    "Moldova": "Chisinau",
    "Monaco": "Monaco",
    "Montenegro": "Podgorica",
    "Netherlands": "Amsterdam",
    "North Macedonia": "Skopje",
    "Norway": "Oslo",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Romania": "Bucharest",
    "Russia": "Moscow",
    "San Marino": "San Marino",
    "Serbia": "Belgrade",
    "Slovakia": "Bratislava",
    "Slovenia": "Ljubljana",
    "Spain": "Madrid",
    "Sweden": "Stockholm",
    "Switzerland": "Bern",
    "Turkey": "Ankara",
    "Ukraine": "Kiev",
    "United Kingdom": "London",
    "Vatican City": "Vatican City"

}


# Loop function for playing the game.
def play_game():
    player = input("Player name: ")
    countries = list(europe_capitals.keys())
    right = 0
    attempts = 0

    with open("capital_score_list.txt", "r") as score_file:
        capital_score_list = json.loads(score_file.read())

    while True:
        country = random.choice(countries)
        capital = europe_capitals[country]
        guess_capital = input("The capital of " + str(country) + " is: ")
        attempts += 1

        if guess_capital == capital:
            right += 1
            print("You are right! :)")
        else:
            print("Wrong. The capital of " + str(country) + " is " + str(capital) + ".")

        choice = input("Bring me more! (y/n): ")
        if choice.lower() != "y" and choice.lower() != "yes":
            capital_score_list.append({"player": player,
                                       "right": right,
                                       "attempts": attempts,
                                       "date": str(datetime.datetime.now())})
            with open("capital_score_list.txt", "w") as score_file:
                score_file.write(json.dumps(capital_score_list))
            print("\nYou guessed " + str(right) + " out of " + str(attempts) + " capitals.\n")
            break


# Get a list of all scores.
def get_all_scores():
    with open("capital_score_list.txt", "r") as score_file:
        capital_score_list = json.loads(score_file.read())
        return capital_score_list


while True:
    selection = input("Would you like to: \n"
                      "P) Test your knowledge, \n"
                      "S) see all scores, \n"
                      "E) exit the quiz: \n")

    if selection.upper() == "P":
        play_game()
    elif selection.upper() == "S":
        print("All scores:")
        for score_dict in get_all_scores():
            score_text = f"Player {score_dict.get('player')} got right {score_dict.get('right')} capitals out of {score_dict.get('attempts')} on {score_dict.get('date')}."
            print("Player Chuck Norris got right ALL capitals out of ALL at ANY TIME.")
            print(score_text)
    else:
        break

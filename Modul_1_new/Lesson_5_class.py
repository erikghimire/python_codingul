#python -m pip install pandas textblob colorama
#csv file https://github.com/krishna-koly/IMDB_TOP_1000/blob/main/imdb_top_1000.csvManya

import os
import pandas as pd
from textblob import TextBlob
from colorama import Fore, init

init(autoreset=True)  # colors reset automatically after each print

# Load the movies (the CSV must be in the same folder as this file)
path = os.path.join(os.path.dirname(__file__), "imdb_top_1000.csv")
df = pd.read_csv(path)

# Every genre, split up: "Action, Drama" -> "Action", "Drama"
genres = sorted(df["Genre"].str.split(", ").explode().unique())


def feeling(text):
    """Return (polarity, label) for a piece of text."""
    p = TextBlob(str(text)).sentiment.polarity  # -1.0 (negative) to +1.0 (positive)
    return p, "Positive 😊" if p > 0 else "Negative 😞" if p < 0 else "Neutral 😐"


def recommend(genre, rating):
    movies = df[df["Genre"].str.contains(genre) & (df["IMDB_Rating"] >= rating)]
    print(Fore.YELLOW + f"\n🍿 Movies for {name}:")
    count = 0
    for _, movie in movies.sample(frac=1).iterrows():  # shuffle for new picks each time
        p, label = feeling(movie["Overview"])
        if p >= 0:  # skip movies whose story sounds negative
            count += 1
            print(Fore.CYAN + f"{count}. 🎥 {movie['Series_Title']} ({label}, {p:.2f})")
            if count == 5:
                return
    if count == 0:
        print(Fore.RED + "No movies found.")


print(Fore.BLUE + "🎥 Welcome to your Movie Recommendation Assistant! 🎥")
name = input(Fore.YELLOW + "What's your name? ").strip()

for i, g in enumerate(genres, 1):
    print(Fore.CYAN + f"{i}. {g}")
choice = ""
while not (choice.isdigit() and 1 <= int(choice) <= len(genres)):
    choice = input(Fore.YELLOW + "Pick a genre number: ").strip()
genre = genres[int(choice) - 1]

mood = input(Fore.YELLOW + "How do you feel today? ")
p, label = feeling(mood)
print(Fore.GREEN + f"Your mood is {label} (Polarity: {p:.2f})")

x = input(Fore.YELLOW + "Minimum IMDB rating (7.6-9.3), or press Enter to skip: ").strip()
rating = float(x) if x.replace(".", "", 1).isdigit() else 0  # anything else = no limit

while True:
    recommend(genre, rating)
    if input(Fore.YELLOW + "\nMore recommendations? (yes/no): ").strip().lower() != "yes":
        break
print(Fore.GREEN + f"Enjoy your movies, {name}! 🎬🍿")
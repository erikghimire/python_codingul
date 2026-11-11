p#pip install colorama
import random
from colorama import Fore, init

init(autoreset=True)  # colors reset automatically after each print

DESTINATIONS = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"],
}


JOKES = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? It had a virus!",
    "Why do travelers always feel warm? All their hot spots!",
]

HELP = "I can: suggest a trip ('recommend'), give packing tips ('pack'), tell a 'joke'. Type 'bye' to leave."


def bot(text, color=Fore.CYAN):
    print(color + "TravelBot: " + text)


def ask(prompt="You: "):
    return " ".join(input(Fore.YELLOW + prompt).lower().split())  # lowercase + tidy spaces


def recommend():
    while True:  # keep going until the user is happy
        bot("Beaches, mountains, or cities?")
        choice = ask()
        if choice not in DESTINATIONS:
            bot("Sorry, I only know beaches, mountains, or cities.", Fore.RED)
            continue
        place = random.choice(DESTINATIONS[choice])
        bot(f"How about {place}? (yes/no)", Fore.GREEN)
        if ask() == "yes":
            bot(f"Awesome! Enjoy {place}!", Fore.GREEN)
            return
        bot("Let's try another.", Fore.RED)


def packing_tips():
    bot("Where to?")
    place = ask()
    bot("How many days?")
    days = ask()
    bot(f"Tips for {days} days in {place}: pack versatile clothes, "
        "bring chargers/adapters, check the weather.", Fore.GREEN)


bot("Hello! What's your name?")
name = input(Fore.YELLOW + "You: ").strip()
bot(f"Nice to meet you, {name}! {HELP}", Fore.GREEN)

while True:
    text = ask(f"{name}: ")
    if "recommend" in text or "suggest" in text:
        recommend()
    elif "pack" in text:
        packing_tips()
    elif "joke" in text or "funny" in text:
        bot(random.choice(JOKES), Fore.YELLOW)
    elif "help" in text:
        bot(HELP, Fore.MAGENTA)
    elif "bye" in text or "exit" in text:
        bot("Safe travels! Goodbye!")
        break
    else:
        bot("Could you rephrase? Type 'help' to see what I can do.", Fore.RED)

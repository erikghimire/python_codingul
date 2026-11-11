#pip install textblob colorama
from colorama import Fore, Style, init
from textblob import TextBlob

init(autoreset=True)  # colors reset automatically after each print

# Label -> (color, emoji)
STYLES = {
    "Positive": (Fore.GREEN, "😊"),
    "Negative": (Fore.RED, "😞"),
    "Neutral": (Fore.YELLOW, "😐"),
}


def analyze(text):
    """Return (polarity, label) for a sentence."""
    polarity = TextBlob(text).sentiment.polarity  # -1.0 (very negative) to +1.0 (very positive)
    if polarity > 0.25:
        return polarity, "Positive"
    if polarity < -0.25:
        return polarity, "Negative"
    return polarity, "Neutral"


def show(text, polarity, label):
    color, emoji = STYLES[label]
    print(f"{color}{emoji} {label} ({polarity:.2f}) {text}")


name = input("Your name: ").strip() or "Mystery Agent"
print(f"{Fore.CYAN}Hello, Agent {name}! Type a sentence, or: history, reset, exit")

history = []

while True:
    text = input(">> ").strip()
    command = text.lower()

    if not text:
        continue
    elif command == "exit":
        print(f"{Fore.BLUE}Goodbye, Agent {name}!")
        break
    elif command == "reset":
        history.clear()
        print("History cleared.")
    elif command == "history":
        for entry in history:
            show(*entry)
        if not history:
            print("No history yet.")
    else:
        polarity, label = analyze(text)
        history.append((text, polarity, label))
        show(text, polarity, label)

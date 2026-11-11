
import colorama

from colorama import Fore, Style

from textblob import TextBlob

colorama.init()

history = []

print(f"{Fore.CYAN}🐍 Sentiment Spy! Type 'exit' to quit.{Style.RESET_ALL}")

name = input(f"{Fore.MAGENTA}Name: {Style.RESET_ALL}").strip() or "Agent"

while True:

text = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

if not text: continue


if text.lower() == "exit": break

if text.lower() == "reset":

history.clear()

print(f"{Fore.CYAN}History cleared!{Style.RESET_ALL}")

continue

if text.lower() == "history":

for i, (t, p, s) in enumerate(history, 1):

print(f"{i}. {t} | {s} ({p:.2f})")

continue

p = TextBlob(text).sentiment.polarity

s = "Positive" if p > 0.25 else "Negative" if p < -0.25 else "Neutral"

c, e = (Fore.GREEN, "😊") if s == "Positive" else (Fore.RED, "😞") if s == "Negative" else (Fore.YELLOW, "😐")


history.append((text, p, s))

print(f"{c}{e} {s} ({p:.2f}){Style.RESET_ALL}")
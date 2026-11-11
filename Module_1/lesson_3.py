
import colorama

from colorama import Fore, Style

from textblob import TextBlob


colorama.int()
user_input = input("enter your mood in one sentence")
polarity = textblob(user_input).sentiment.polarity
sentiment = ""
emoji = ""
if polarity > 0.25:
    sentiment = "positive"
    emoji = "😊"
    
elif polarity < -0.25 :
    sentiment = "negitive"
    emoji = "😞"
else:
    sentiment = "neutral"

    emoji = "😭"
print(f"{Fore.YELLOW}{emoji} {sentiment} sentiment detected! ")


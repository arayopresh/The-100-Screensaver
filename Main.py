import time
import random
import os


def load_quotes(): #function to load the file from quotes.txt
    try:
        with open("Quotes.txt", "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()] # skips the blanks and removes empty spaces so it can read each line
    except FileNotFoundError: #theow exception when the txt file is empty
       return ["Quotes.txt file is empty. Nothing to display."]
    
def display_quotes():
    quotes = load_quotes()
    while True:
        quote = random.choice(quotes)
        print(quote)
        time.sleep(1)
        exit = input("Press q to exit").upper
        if exit == 'q':
            break

display_quotes()


    

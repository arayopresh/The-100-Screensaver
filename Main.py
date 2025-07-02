import time
import random
import tkinter as tk #pop up



def load_quotes(): #function to load the file from quotes.txt
    try:
        with open("Quotes.txt", "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()] # skips the blanks and removes empty spaces so it can read each line
    except FileNotFoundError: #theow exception when the txt file is empty
       return ["Quotes.txt file is empty. Nothing to display."]
    

'''def display_quotes():
    counter = [0]
    max_quotes = 100 #maximum number of quotes allowed to be displayed
    quotes = load_quotes()
   while counter < max_quotes:
        quote = random.choice(quotes)
        print(quote)
        time.sleep(1) #will it freeze the gui??
        counter = counter + 1  '''

#window for display
root = tk.Tk()
root.title("The 100")
root.geometry("600x200")


# hiw the quotes aere gonna look
quote_label = tk.Label(root, text="", wraplength=500, font=("Times New Roman", 30), justify="left")
quote_label.pack() #i dont want it expanding down

#sayer of quote
quote_sayer = tk.Label(root, text = "", wraplength = 500, font = ("Times New Roman", 20, "italic"), justify = "right")
quote_sayer.pack() 




counter = [0] #using a list here bc i might wanna modify
max_quotes = 100 #maximum number of quotes allowed to be displayed
quotes = load_quotes()

def quotes_display():
    if counter[0] < max_quotes:
        full_quote = random.choice(quotes) #random choice of quotes

       # print(f"Displaying quote {counter[0]+1}: {full_quote}")

        # Split the quote and author
        if '-' in full_quote:
            quote_text, author = full_quote.split('-', 1)  # splits the first dash only
            quote_label.config(text=quote_text.strip())
            quote_sayer.config(text=f"— {author.strip()}")
        else:
            quote_label.config(text=full_quote)
            quote_sayer.config(text="")
        counter[0] += 1
        root.after(1000, quotes_display) #changes every 10 secs
    else:
            root.destroy() #will automatically close the window after 100 quotes have veen showed

    

#display_quotes()

quotes_display() 
root.mainloop()


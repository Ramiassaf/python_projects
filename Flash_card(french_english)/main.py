import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# --------------------------Flash Card Setup------------------------- #
# Initialize the current card dictionary
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("words_to_learn.csv")  # Attempt to read data from "words_to_learn.csv" file
except FileNotFoundError:  # If the file is not found, handle the FileNotFoundError
    original_data = pd.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")   # Convert the data to a list of dictionaries
else:  # If the "words_to_learn.csv" file exists, proceed with this branch
    to_learn = data.to_dict(orient="records")   # Convert the data from "words_to_learn.csv" to a list of dictionaries



def next_card():  # Function to display the next flashcard
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # Cancel the previous timer
    current_card = random.choice(to_learn)
    # Update the text on the canvas to display the French word
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(canvas_image, image=old_image)
    # Schedule this function to run again after 3 seconds
    flip_timer = window.after(3000, func=flip_card)  # 3 seconds


# --------------------------Flipper Setup & Timer Setup------------------------- #


def flip_card():  # Function to flip the flashcard and change the display
    global current_card
    # Update the text on the canvas to display the English translation
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    # Change the canvas image to display the back of the card
    canvas.itemconfig(canvas_image, image=new_image)


# ---------------------Known Button Setup--------------------- #
def known():
    to_learn.remove(current_card)  # Remove the 'current_card' from the 'to_learn' list
    words_to_learn = pd.DataFrame(to_learn)  # Convert the updated 'to_learn' list into a DataFrame
    words_to_learn.to_csv("words_to_learn.csv", index=False)  # Save the DataFrame to a CSV file named
    # 'words_to_learn.csv' without the index
    # Call a function to display the next card (Assuming you have a function for this purpose)
    next_card()

# --------------------------UI SETUP------------------------- #


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Schedule the flip_card function to run after 3 seconds
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_logo = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_logo)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)  # columnspan=2 means 2 columns

# Create PhotoImage objects for the front and back images
new_image = PhotoImage(file="images/card_back.png")
old_image = PhotoImage(file="images/card_front.png")

# Create a canvas image element for displaying the flashcard
canvas_image = canvas.create_image(400, 263, image=old_image)

# Text
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, command=next_card, highlightthickness=0)
unknown_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, command=known, highlightthickness=0)
known_button.grid(row=1, column=1)

# Initial display of the first flashcard
next_card()

# Start the Tkinter main loop
window.mainloop()

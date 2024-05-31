from tkinter import *
import random
import pandas

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- PANDAS ------------------------------- #
try:
    df = pandas.read_csv("data/words_to_learn.csv")
    df_dict = df.to_dict(orient="records")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")
    df_dict = df.to_dict(orient="records")


# ---------------------------- Functions ------------------------------- #
current_word = {}


def new_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(df_dict)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(answer_text, text=current_word['French'],  fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_word
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(answer_text, text=current_word['English'], fill="white")


def card_correct():
    df_dict.remove(current_word)
    data = pandas.DataFrame(df_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_card()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashcard Madness")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(405, 270, image=card_front_img)

language_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
answer_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

flip_timer = window.after(3000, func=flip_card)


# Buttons

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, command=new_card)
wrong_button.grid(column=0, row=1)

correct_button_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_button_img, command=card_correct)
correct_button.grid(column=1, row=1)

new_card()


window.mainloop()

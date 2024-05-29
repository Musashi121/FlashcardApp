from tkinter import *
import random
import pandas

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- PANDAS ------------------------------- #

df = pandas.read_csv("data/french_words.csv")
df_dict = df.to_dict(orient="records")


# ---------------------------- Functions ------------------------------- #
def new_card():
    current_word = random.choice(df_dict)
    canvas.itemconfig(language_text, text="French")
    canvas.itemconfig(answer_text, text=current_word['French'])


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashcard Madness")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(height=526, width=800)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(405, 270, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
language_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
answer_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)



# Buttons

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, command=new_card)
wrong_button.grid(column=0, row=1)

correct_button_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_button_img, command=new_card)
correct_button.grid(column=1, row=1)

new_card()


window.mainloop()

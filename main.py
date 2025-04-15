from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# CREATING THE WINDOWS AND CANVAS
window = Tk()
canvas  = Canvas()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
canvas.config(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row = 0,column = 0,rowspan = 2, columnspan = 2)
window.title("words teller")


# LOADING THE DATAFRAME
header = ["German","English"]
try:
     data = pd.read_csv("words_to_learn.csv",names=header)
except FileNotFoundError:
     data = pd.read_csv("PYTHON_CAPSTONE_PROJECT_DATA.csv", names=header)

df = pd.DataFrame(data)
dict_of_words = df.to_dict(orient="records")

german_text = {}
flip_timer = None

def remove_known_words():
     """It removes the word that is correctly selected and remove it from the CSV file"""
     dict_of_words.remove(german_text)
     new_dataframe = pd.DataFrame(dict_of_words)
     new_dataframe.to_csv(path_or_buf="words_to_learn.csv",index=False,header=False)
     words()
     # dict_of_words.t(path_or_buf="PYTHON_CAPSTONE_PROJECT_DATA.csv")

def english_words():
     print(german_text)
     """This will update the heading and the word in english"""
     canvas.itemconfig(heading_id,text = "English",fill="white")
     canvas.itemconfig(answer_id,text=german_text['English'],fill="white")
     canvas.itemconfig(image_id,image=back_side_canvas)

def words():
     """This will display the words in german and updates the flash card and calls the english_words function"""
     global german_text,flip_timer
     if flip_timer is not None:
          window.after_cancel(flip_timer)

     german_text = random.choice(dict_of_words)
     canvas.itemconfig(heading_id,text="German",fill="black")
     canvas.itemconfig(answer_id,text=german_text["German"],fill="black")
     canvas.itemconfig(image_id,image=front_side_canvas)
     flip_timer = window.after(3000,func=english_words)


front_side_canvas = PhotoImage(file="./images/card_front.png")
back_side_canvas = PhotoImage(file="./images/card_back.png")
image_id = canvas.create_image(400,263,image=front_side_canvas)

# CREATING THE HEADING TEXT
heading_id = canvas.create_text(400,150,font=("Arial",40,"italic"),fill = "black")
canvas.itemconfig(heading_id,text="German")

# CREATING THE ANSWER TEXT
answer_id = canvas.create_text(400,263,font=("Arial",40,"bold"))
canvas.itemconfig(answer_id,text=words())

# CREATING THE  BUTTONS
button_image_right = PhotoImage(file="./images/right.png") # WRONG IMAGE
button1 = Button(image=button_image_right,highlightthickness=0,bg=BACKGROUND_COLOR,command=remove_known_words)
button1.grid(row=2,column=1)

button_image_left = PhotoImage(file="./images/wrong.png") # CHECK IMAGE
button1 = Button(image=button_image_left,highlightthickness=0,bg=BACKGROUND_COLOR,command=words)
button1.grid(row=2,column=0)


window.mainloop()






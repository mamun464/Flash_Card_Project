BACKGROUND_COLOR = "#B1DDC6"

from randomWord import *
from tkinter import messagebox
from tkinter import *
single_word_dict={}

#-----------------------POP UP window-----------------------

#-----------------------Create New Flash Cards-----------------------
def generateWord():
    global single_word_dict,flip_timer
    windos.after_cancel(flip_timer)
    #single_word_dict=getWord()
    single_word_dict=getWord_with_check_save()

    canvas.itemconfig(cardBG, image=card_front)
    canvas.itemconfig(wordCagory, text="Bangla",fill="black")
    try:
        canvas.itemconfig(word_posi, text=single_word_dict["Bangla"],fill="black")
    except TypeError:
        print("Press again Bangla")
        single_word_dict = getWord_with_check_save()
    flip_timer=windos.after(3000, func=Flip_card)

def Flip_card():
    global single_word_dict
    canvas.itemconfig(cardBG, image=card_back)
    canvas.itemconfig(wordCagory, text="English",fill="white")
    try:
        canvas.itemconfig(word_posi, text=single_word_dict["English"],fill="white")
    except TypeError:
        print("Press again English")
        single_word_dict = getWord_with_check_save()


def isKnown():
    global single_word_dict
    with open("data/all_ready_learn.csv", "a", encoding='utf-8') as file:
        # f"{single_word['Bangla']},{single_word['English']}\n"
        file.write(f"{single_word_dict['Bangla']},{single_word_dict['English']}\n")
        print(f"return: {single_word_dict}")

    generateWord()


    #print(bangla_english_dict)
#-----------------------UI SetUp--------------------------------------
windos=Tk()
windos.title("Flashy")
windos.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=windos.after(3000, func=Flip_card)

canvas=Canvas(width=800,height=526)
card_front=PhotoImage(file="images/card_front.png")
card_back=PhotoImage(file="images/card_back.png")
cardBG=canvas.create_image(400,263,image=card_front)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
wordCagory=canvas.create_text(400,150,text="", font=("Ariel",40,"italic"))
word_posi=canvas.create_text(400,263,text="", font=("Ariel",50,"bold"))
canvas.grid(row=0,column=0,columnspan=2)


wrong=PhotoImage(file="images/wrong.png")
unknown_btn=Button(image=wrong, highlightthickness=0,bg=BACKGROUND_COLOR,command=generateWord)#
unknown_btn.grid(row=1, column=0)

right=PhotoImage(file="images/right.png")
check_btn=Button(image=right,highlightthickness=0,bg=BACKGROUND_COLOR,command=isKnown)
check_btn.grid(row=1,column=1)


generateWord()


windos.mainloop()

import csv
import os
import random
import sys
from tkinter import messagebox

# from main import windos

import pandas as pd

all_word_List = pd.read_csv("data/bangla_words.csv")
banglaEnglish_word_dict={row.Bangla:row.English for (index,row) in all_word_List.iterrows()}
alreadyLearn_word_dict={}
all_ready_learn=[]
def fileGenerate():
    global all_ready_learn
    try:
       all_ready_learn=pd.read_csv("data/all_ready_learn.csv")

    except FileNotFoundError:
        with open("data/all_ready_learn.csv","w") as file:
            file.write("Bangla,English\n")


fileGenerate()

def getWord():
    global banglaEnglish_word_dict,all_word_List
    bangla=random.choice(list(banglaEnglish_word_dict.keys()))
    english=banglaEnglish_word_dict.get(bangla)
    singleWord_dict={
        "Bangla":bangla,
        "English":english
    }
    #print(singleWord_dict)
    return singleWord_dict

#def getWord_with_check_save():

x={
        "Bangla":"আমি",
        "English":"I"
    }
def getWord_with_check_save():
    global banglaEnglish_word_dict,alreadyLearn_word_dict,x
    all_ready_learn = pd.read_csv("data/all_ready_learn.csv")
    alreadyLearn_word_dict = {row.Bangla: row.English for (index, row) in all_ready_learn.iterrows()}
    single_word=getWord()
    print(f"start: {single_word}")

    if single_word["Bangla"] in alreadyLearn_word_dict:
        if len(alreadyLearn_word_dict) == len(banglaEnglish_word_dict):
            isOk = messagebox.showinfo(title="DONE",
                                       message=f"Congratulations 🥳\nYou Complited all {len(alreadyLearn_word_dict)} words!")

            if isOk:
                print("canceling")
                os.remove("data/all_ready_learn.csv")
                sys.exit()
        else:
            getWord_with_check_save()
            print("already learn")




    else:
        # with open("data/all_ready_learn.csv","a",encoding='utf-8') as file:
        #     #f"{single_word['Bangla']},{single_word['English']}\n"
        #     file.write(f"{single_word['Bangla']},{single_word['English']}\n")
        #     print(f"return: {single_word}")
            return single_word




print(alreadyLearn_word_dict)




# x=getWord()
# print(x["Bangla"].strip())
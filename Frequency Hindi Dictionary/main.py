from tkinter import *
import pandas
from random import randint

english_word =' '
hindi_word =' '
random_number=1000
BACKGROUND_COLOR = "#B1DDC6"
words_learned={"Hindi": [], "English": []}

content = pandas.read_csv('data/hindi_words.csv')
#print(content)
content_dict= content.to_dict(orient="records") #converting to dictionary
#print(content_dict)
word_list=content['Hindi'].to_list()
english_list=content['English'].to_list()
random_number= randint(0,len(word_list))
#print(random_number)

hindi_word=word_list[random_number]
english_word=english_list[random_number]

window = Tk ()
window.title("Learn Hindi Basics in a Week")
window.config(bg=BACKGROUND_COLOR,padx=50, pady=50)


def generate_word():
    global english_word
    global hindi_word
    global random_number
    try:
        random_number = randint(1, len(word_list)+1)
    except IndexError:
        pass
    hindi_word = word_list[random_number]
    english_word = english_list[random_number]
    word.config(text=hindi_word, fg='black', bg='white')
    language.config(text='Hindi', fg='black',bg='white')
    canvas.itemconfig(card_background, image=card_img)
    canvas.after(3000, answer_card)


def wrong_ans():
    generate_word()

eng_word=[]
def correct_ans():
    words_learned["Hindi"]=hindi_word
    words_learned["English"]=english_word
    try:
        content_dict.remove(words_learned)
        content = pandas.DataFrame(content_dict)
    except:
        print('removed already')
    eng_word.append(english_word)
    with open('learned.txt','w') as learn:
        learn.write(str(eng_word))
    content = pandas.DataFrame
    generate_word()


def answer_card():
    language.config(text="English", fg='white', bg='#7eca9c')
    word.config(text=english_word,fg='white', bg='#7eca9c')
    canvas.itemconfig(card_background, image=card_back_img)





canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_img=PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background= canvas.create_image(405,263,image=card_img)
canvas.grid(row=0,column=0,columnspan=2)
canvas.after(3000, answer_card)

language=Label(text="Hindi", font=("Ariel",40,"italic"))
language.place(x=300, y=50)
language.config(bg='white')

word=Label(text=hindi_word, font=("Ariel",60,"bold"))
word.place(x=300, y=250)
word.config(bg='white')

wrong_image=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_image,command=wrong_ans,highlightthickness=0)
wrong_button.grid(row=1, column=0)

correct_image=PhotoImage(file="images/right.png")
correct_button=Button(image=correct_image,command=correct_ans,highlightthickness=0)
correct_button.grid(row=1, column=1)



window.mainloop()


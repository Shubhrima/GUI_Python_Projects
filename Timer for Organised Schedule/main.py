from tkinter import *
import turtle
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WORK_MIN = .25
SHORT_BREAK_MIN = .05
LONG_BREAK_MIN = .4
REPEAT = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    check.config(text=" ")
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg="GREEN")
    global REPEAT
    REPEAT=1
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPEAT
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if REPEAT%2!=0:
        count_down(work_sec)
        label.config(text="Work Mode On", fg=GREEN)
    elif REPEAT%8==0:
        count_down(long_break_sec)
        label.config(text="Long Break", fg=RED)
    else:
        count_down(short_break_sec)
        label.config(text="Short Break", fg=PINK)
    print(REPEAT)
    REPEAT += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count>=0:
        global timer
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        timer=window.after(1000,count_down, count-1)
    else:
        start_timer()
        marks= ""
        work=math.floor(REPEAT/2)
        for _ in range(work):
            marks+= "✔"
        check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Set The Timer")
window.minsize(width=500, height=500)
window.config(bg=YELLOW,padx=100, pady=50)


label=Label(text="Timer",font=('Courier',25,'bold'))
label.config(bg=YELLOW, fg="GREEN")
label.grid(row=0,column=1)

canvas=Canvas(width=200, height=240, bg=YELLOW,highlightthickness=0)
timer_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=timer_img)
timer_text=canvas.create_text(100,120,text="00:00",fill='white', font=('Courier',25,'bold'))
canvas.grid(row=1,column=1)

button_set=Button(text='Set',command=start_timer)
button_set.grid(row=2,column=0)
button_set.config(padx=5, pady=5)

button_reset=Button(text='Reset', command=reset_timer)
button_reset.grid(row=2,column=2)
button_reset.config(padx=5, pady=5)

check=Label(font=('Arial',25,'bold'))
check.config(bg=YELLOW, fg=GREEN)
check.grid(row=3,column=1)



window.mainloop()
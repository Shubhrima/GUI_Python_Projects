from tkinter import *

window= Tk()
window.title('Temperature Converter')
window.minsize(width=500, height=300)
window.config(padx=50,pady=50)

label=Label(text='Covert form Celcius to Fahrenheit:',font=('Courrier',25,'bold'))
label.grid(column=2, row=0)
label.config(pady=10)

input=Entry()
input.grid(row=2,column=2)

ans=Label(text=' ',font=('Courrier',10,'bold'))
ans.grid(row=4,column=2)

def convert():
    temp = float(input.get())
    temp_F= temp*9/5+32
    ans['text']='Temperature in Fahrenheit is: '+str(int(temp_F))


button=Button(text='Covert', command=convert)
button.grid(row=2,column=3)








window.mainloop()
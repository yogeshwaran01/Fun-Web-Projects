from tkinter import *
import random
import time
master = Tk()
master.title("STONE PAPER SCISSOR")
def stone():
    e1.insert(0," stone ")
    a=random.choice([" stone "," paper "," scissor "])
    e2.insert(0,a)
    if a==" stone ":
        e3.insert(0," draw ")
    elif a==" paper ":
        e3.insert(0," CPU ")
    elif a==" scissor ":
        e3.insert(0," YOU ")
    else:
        e3.insert(0," error ")
def paper():
    e1.insert(0, " paper ")
    a = random.choice([" stone ", " paper ", " scissor "])
    e2.insert(0, a)
    if a == " stone ":
        e3.insert(0, " YOU ")
    elif a == " paper ":
        e3.insert(0, " draw ")
    elif a == " scissor ":
        e3.insert(0, " CPU ")
    else:
        e3.insert(0, " error ")
def scissor():
    e1.insert(0, " scissor ")
    a = random.choice([" stone ", " paper ", " scissor "])
    e2.insert(0, a)
    if a == " stone ":
        e3.insert(0, " CPU ")
    elif a == " paper ":
        e3.insert(0, " YOU ")
    elif a == " scissor ":
        e3.insert(0, " draw ")
    else:
        e3.insert(0, " error ")

def playagain():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)

lplay=Label(text="YOU").grid(row=0,column=1)
lcpu=Label(text="CPU").grid(row=0,column=2)
btn1=Button(master,text="stone",command=stone).grid(row=1,column=0)
btn2=Button(master,text="paper",command=paper).grid(row=2,column=0)
btn3=Button(master,text="scissor",command=scissor).grid(row=3,column=0)
btn3=Button(master,text="play again",command=playagain).grid(row=4,column=2)
ldis=Label(text="winner:").grid(row=3,column=1)
e1=Entry(master,width=20,borderwidth=10)
e2=Entry(master,width=20,borderwidth=10)
e3=Entry(master,width=20,borderwidth=10)
e1.grid(row=2,column=1)
e2.grid(row=2,column=2)
e3.grid(row=3,column=2)

master.mainloop()

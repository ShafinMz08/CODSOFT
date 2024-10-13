from tkinter import *
import random, string


var = Tk()
var.geometry("400x280")
var.title("Password Generator Application")

title = StringVar()
label = Label(var, textvariable=title).pack()
title.set("CHOOSE AN OPTION")


def selection():
    global selection
    selection = choice.get()



choice = IntVar()
R1 = Radiobutton(var, text="WEAK password", variable=choice, value=1, command=selection).pack(anchor=CENTER)
R2 = Radiobutton(var, text="AVERAGE password", variable=choice, value=2, command=selection).pack(anchor=CENTER)
R3 = Radiobutton(var, text="STRONG password", variable=choice, value=3, command=selection).pack(anchor=CENTER)
labelchoice = Label(var)
labelchoice.pack()


lenlabel = StringVar()
lenlabel.set("Password length:")
lentitle = Label(var, textvariable=lenlabel).pack()


val = IntVar()
spinlenght = Spinbox(var, from_=4, to_=24, textvariable=val, width=13).pack()



def callback():
    lsum.config(text=passgen())



passgenButton = Button(var, text="Generate Password", bd=5, command=callback)
passgenButton.pack(pady=20)
password = str(callback)


lsum = Label(var, text="Password here", font=("arial", 20))
lsum.pack(side=BOTTOM, anchor="n")


poor= string.ascii_uppercase + string.ascii_lowercase
average= string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
advance = poor+ average + symbols


def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance, val.get()))


var.mainloop()

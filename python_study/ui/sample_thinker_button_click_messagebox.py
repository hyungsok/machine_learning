from tkinter import *
from tkinter import messagebox


def okClick():
    name = txt.get()
    messagebox.showinfo("Name", name)


window = Tk()
lbl = Label(window, text="Name")
lbl.grid(row=0, column=0)
txt = Entry(window)
txt.grid(row=0, column=1)

btn = Button(window, text="OK", command=okClick)
btn.grid(row=1, column=1)

window.mainloop()

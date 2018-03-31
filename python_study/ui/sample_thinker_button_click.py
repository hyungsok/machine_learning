from tkinter import *

def process():
    print(">> Hello?")

window = Tk()
btn = Button(window, text="Click", command=process)
btn.pack()
window.mainloop()
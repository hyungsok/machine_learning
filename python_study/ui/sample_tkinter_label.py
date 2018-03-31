from tkinter import *
root = Tk()

lbl = Label(root, text="Name")
lbl.pack() # 배치

txt = Entry(root)
txt.pack()

btn = Button(root, text="OK")
btn.pack()

# 해당 코딩을 넣어줘야 그려줌 
root.mainloop()
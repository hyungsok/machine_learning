# coding:euc-kr

from tkinter import *


class Win:
    def __init__(self):
        w = Tk()
        w.title('��ǰ����')
        self.v = IntVar()
        r1 = Radiobutton(w, text='���', variable=self.v, value=1000, command=self.se)
        r2 = Radiobutton(w, text='����', variable=self.v, value=2000, command=self.se)
        r3 = Radiobutton(w, text='����', variable=self.v, value=20000, command=self.se)
        r4 = Radiobutton(w, text='����', variable=self.v, value=4000, command=self.se)

        self.count = IntVar()
        e1 = Entry(w, textvariable=self.count)
        l1 = Label(w, text='����')
        b1 = Button(w, text='���', command=self.calc)
        self.l2 = Label(w, text='�ѱݾ� : ')

        r1.grid(row=1, column=1)
        r2.grid(row=2, column=1)
        r3.grid(row=3, column=1)
        r4.grid(row=4, column=1)
        l1.grid(row=5, column=1)
        e1.grid(row=5, column=2)
        b1.grid(row=5, column=3)
        self.l2.grid(row=6, column=1)

        w.mainloop()

    def se(self):
        pass

    def calc(self):
        result = '�ѱݾ� : '
        result += str(self.v.get() * self.count.get())
        self.l2['text'] = result
        print()


Win()

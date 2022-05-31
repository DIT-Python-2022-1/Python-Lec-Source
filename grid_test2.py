from tkinter import *

win = Tk()
win.geometry("250x80")

def show():
    print(e1.get(), e2.get())
    ## 다음을 위하여 Entry 초기화 하기
    e1.delete(0, END)
    e2.delete(0, END)
    e1.focus_set()

l1 = Label(win, text='이름')
l2 = Label(win, text='나이')
l1.grid(row=0, column=0)
l2.grid(row=1,column=0)

e1 = Entry(win, width=14)
e2 = Entry(win, width=14)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(win, text='보기', width=8, command=show)
b2 = Button(win, text='끝내기', width=8, command=exit)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)

win.mainloop()
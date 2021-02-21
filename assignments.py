from tkinter import *
from timeit import default_timer as timer 
import random 

window = Tk()
window.geometry("450x200")
Title=Label(window,text="lets start this game ...", font="times 20")
Title.place(x=10,y=50)

def speedtest_game():
    print(" ")

b1=Button(window,text="goo",command=speedtest_game,width=12,bg='gray')
b1.place(x=150,y=100)


Title.pack()
window.mainloop()
'''
windows.geometry("450x200")
x1=label(window,text="lets start this game ...", font="times 20")
x1.place(x=10, y=50)

def game():
    print("")
b1=Button(window,text="goo",command=game,width=12,bg='gray')
b1.place(x=150,y=100)

window.mainloop()'''
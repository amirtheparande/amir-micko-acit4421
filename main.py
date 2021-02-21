from tkinter import *
from timeit import default_timer as timer 
import random 

window = Tk()
window.geometry("450x200")
Title=Label(window,text="lets start the counter!", font="times 20")
Title.place(x=10,y=50)

def counter_click():
    print(" ")

b=Button(window,text="Click me ",command=counter_click,width=12,bg='gray')
b.place(x=150,y=100)

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
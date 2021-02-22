#imports
from tkinter import *
from timeit import default_timer as timer 
import random 

#Creating the tk window
window = Tk()
window.geometry("450x200")
Title=Label(window,text="lets start the counter!", font="times 20")
Title.place(x=10,y=50)
window.counter = 0

#Increasing the counter by 1 everytime the button is clicked.
def counter_click():
    window.counter += 1
    Title['text'] = 'Button clicked: ' + str(window.counter)

#Killing the window when the button is pressed.
def counter_kill():
    window.destroy()

#Creates the button for the counter
b1=Button(window,text="Click me ",command=counter_click,width=12,bg='gray')
b1.place(x=150,y=100)

#Creates the button to end the counter
b2=Button(window,text="End Counter",command=counter_kill,bg='red')
b2.place(x=150,y=130)

#Pushes gui to Desktop
Title.pack()
window.mainloop()

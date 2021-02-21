#function for cycling through the #s and killing the counter

from Tkinter import *


#Creating the tk window
window = Tk()
window.counter = 0

#This function increases the counter by 1 everytime the button is clicked.
def counter_click():
    window.counter += 1
    Title['text'] = 'Button clicked: ' + str(window.counter)
        

#This function kills the window, when the button is pressed.
def counter_kill():
	window.destroy()


window.mainloop()
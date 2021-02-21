from Tkinter import *

root = Tk()
root.counter = 0

#This function increases the counter by 1 everytime the button is clicked.
def counter_click():
    root.counter += 1
    L['text'] = 'Button clicked: ' + str(root.counter)
        

#This function kills the window, when the button is pressed.
def counter_kill():
	root.destroy()


root.mainloop()
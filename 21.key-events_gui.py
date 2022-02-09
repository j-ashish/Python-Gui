from tkinter import *

def dosomething(event): # Binded key return the value so get that value we have to pass the variable to access that value and perfrom some action.
    print("You Pressed The Enter Button")
    

window = Tk()

# This function binds the key to a function to do some sort of work after pressing that key. Sytnax is as follows, key to bind in the angular brackets and the function that is going to perform some action. Example: root.bind(<key_name>,function_name)
window.bind("<Up>",dosomething)


window.mainloop()
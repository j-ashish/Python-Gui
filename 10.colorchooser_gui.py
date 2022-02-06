from tkinter import *
from tkinter import colorchooser # this is a submodule of an module (TKINTER).

# this program will let the user choose the color.

def click():
    color = colorchooser.askcolor() # colorchooseraskcolor asks color from user with whole color pallete.
    print(color) # here we get the value of the color, which is in two part as a list 1. RGB (-,-,-)  2. Hex Color Value. #------
    colorhex = color[1] # here we assigned the the hex color to the variable because hex colors are readable rather than RGb value.
    print(colorhex)
    window.config(bg=colorhex) # here we configured the main window backgroundcolor.

window = Tk()
window.geometry('420x420')
button = Button(text='click me',
command = click # on click the background of the screen or root window will change.
)

button.pack()
window.mainloop()
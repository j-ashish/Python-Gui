
from tkinter import *

# button = you click it, then it does stuff

count = 0

def click():
    global count
    count+=1 # this function is going to activate on every count and as we set the count variable to global so it will change the value on every execution. And prints the count every time it will be clicked on the console.
    print(count)

window = Tk()

photo = PhotoImage(file='.\\images\\foodbar.png')

button = Button(window, # Button is to set the variable as a Gui button. Window is the main instance of the program.
                text="click me!", # text is used to display the text on the button.
                command=click, # command function is used to instruct the button to do some pre-defined functions. Here whenever the used is going to click on the button a function will be triggerd and it start count on every click.
                font=("Comic Sans",30), # font function is used to set the font type of the text over the button and the size of the text to show.
                fg="#00FF00", # fg is foreground color (Text color)
                bg="black", # bg is for background color which is used to set the background color of the button.
                activeforeground="#00FF00", # activeforeground means here when user click on the button sudden the the text changes to a default color, so here we can change that y putting the color whatever the user like to activate the color on the activation the button.
                activebackground="black", # it is same as the active foreground but in this case it changes the color of the bakcground of the button.
                state=ACTIVE, # state function set, that the button is going to work or not. By default it is always active but it can be changed to DISABLED in case for some reason it has to disabled.
                image=photo, # it set the image over the button, but it hides the text over the button that we put earlier.
                compound='bottom') # here we can set the position of the image so it didn't cover the text we put on the button. (top,bottom,left,right)
button.pack() # here pack is used to pack all the stuff and functions in the variable to use.

window.mainloop()
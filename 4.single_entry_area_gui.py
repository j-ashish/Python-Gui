from tkinter import *

#entry widget = textbox that accepts a single line of user input

def submit():  # On every click this function prints the text entered by the user and the message on the console.
    username = entry.get()  # get function here is used to get the value of the textbox on click.
    print("Hello "+username)

def delete():
    entry.delete(0,END)  # .delete takes to arguments first for the  starting_position or from and second for 'to' ending_position. (Integer indexing) or END to indicate the end of the string.

def backspace():
    entry.delete(len(entry.get())-1, END) # same function is used like before but now we take the length of the whole string and irradicate 1 value from the end.

window = Tk()

entry = Entry(window, # Entry function is used to make the variable to be used as the text-area for the input by the user.
              font=("Arial",50), # font is used to set the font of the user input.
              fg="#00FF00", # fg here is used to set the color of the input text.
              bg="black") # bg here is used to set the background color of the textarea.

#entry.insert(0,'Spongebob')  # .insert is used to put the placeholder text in the textarea (But this text is not like html placeholder it can be).
#entry.config(show="*")  # show attribute of the config function is used to set visual of the text. Like when password is typed and the charachter are in astrisk.
#entry.config(state=DISABLED) # state here is set to disabled to stop user to enter any text.

entry.pack(side=LEFT) # here side attribute instruct the textarea to where to show on the screen.

submit_button = Button(window,text="submit",command=submit) # whenever user is going to click this button, function named submit will be trigerred.
submit_button.pack(side=RIGHT)

delete_button = Button(window,text="delete",command=delete) # whenever user is going to click this button, function named delete will be trigerred.
delete_button.pack(side=RIGHT)

backspace_button = Button(window,text="backspace",command=backspace) # whenever user is going to click this button, function named delete will be trigerred.
backspace_button.pack(side=RIGHT)

window.mainloop()
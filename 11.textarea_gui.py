from tkinter import *

# text widget = functions like a text area , you can enter multiple lines of text.

def submit():
    textvalue = text.get("1.0",END) # get the value that is retrived from the element, from and the end.
    print(textvalue)


window = Tk()

text = Text(window, # text is used to create a textarea.
bg= "#EFCD57",
font = ("Ink Free",25),
height = 8, # Here the height is defined as the number of lines.
width = 20, # Here the width is defined as the number of words in a line.
padx = 20,
pady=20,
fg = "purple",
)
text.pack()

button = Button(window,
text = "Submit",
command = submit, # on the submission the text on the textarea will print on the console window.
)
button.pack()

window.mainloop()
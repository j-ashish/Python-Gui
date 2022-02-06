from tkinter import *
from tkinter import filedialog

# in this program we are going to retrive the value from the text area and we will save it for future use.


def save_file():
    # filedialog.asksaveasfile is used to provide as save as file prompt.
    file = filedialog.asksaveasfile(

        # defaultextension is used to put the deafult action when saving a new file.
        defaultextension='.txt',

        # file type is used to put the list of file types for the user. to save the file as per user need.
        filetypes=[
            #The arguments should be passed in between the brackets. The syntax for the file types to instruct is to create a tuple, first argument is the string that user is going to see for their compatbilty and the second parameter is used to determine the type of the file. ("String",".file_extensnion")
            ("Text File", ".txt"),
            ("HTML File", ".html"),
            # to select the all type of the file the parameter for the file type is to put the dot_notation along with the astrisk to instruct all.
            ("All Files", ".*")],

    )

    # to avoid the error on the empty submission enter this code here after the function.
    #if file is None:
        #return

    # Here we assign a variable with the value inside the textarea. We turned the whole value into the string to get the value with no error, and we set the index of the value that we get from the user is From the beginning or 1.0 and till the end END.
    filetext = str(text.get("1.0", END))

    # in that file we are going to save the file we assign the whole value in it with the python write function.
    file.write(filetext)

    # it is not mandatory but it is a good practice to close the file after the use.
    file.close()


window = Tk()

button = Button(text="Save File",
                command=save_file)
button.pack(side=BOTTOM)

text = Text(window,
            font=("Arial", 10),
            height=10,
            width=40)
text.pack()

window.mainloop()

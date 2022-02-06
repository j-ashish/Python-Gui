from tkinter import *
from tkinter import filedialog


# here we are going to create the openfile dialog box so we can open and read some files through it.


def openfile():
    filepath = filedialog.askopenfilename(  # this will return the file directory or the path associated with the file.
        # this function is used to instruct the file manager where to look at first as a default directory.
        initialdir="C:\\Users\\ASHISH\\Desktop\\Python GUI",

        # this is to put the title on the file dialog box.
        title='open file',

        # first parameter is for prompt and the second parameter is for the type of the file or format after the * with dot notation. We can pass another option just with the first option like : ("All Files","*.*"). In the above example we put the comma after the first parameter because it is a tuple, and to define a tuple or pass a single tuple a comma is necessary after.
        filetypes=(("text file", "*.txt"),),


    )
    # here we know what is the directory that is returned by the above function in an variable.
    print(filepath)

    # here we open that file with python open function along with the mode which is currently 'r' for read.
    file = open(filepath, 'r')

    # here we print the all the file values or data in a console with the read method.
    print(file.read())

    # it isn't neccessary but it is a good practice to close the files after opening.
    file.close()


# root below:-

window = Tk()


button = Button(text="Open",
                command=openfile,
                )
button.pack()

window.mainloop()

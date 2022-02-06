from tkinter import *
from tkinter import messagebox
# messagebox is an element in the tkinter module, so we inherited it here to use it without targeting the parent library.

def click():
    # messagebox.showinfo( # showinfo is used to show a pop up click menu with information sign on it (informatory with Blue sign).
    #     title="This is an information box.", # the title of the pop-up box.
    #     message="Information") # the message inside the pop-up window.
    # messagebox.showwarning( # showwarning is used to show a pop up click menu with CAUTION sign on it (Warning with Yellow sign).
    #     title = "Show Warning",
    #     message="Warning")
    # messagebox.showerror(# showerror is used to show a pop up click menu with ERROR sign on it (Error with Red sign).
    #     title="Shows Error",
    #     message="Something Went Wrong")

    # if messagebox.askokcancel( # this show pop-up window with a prompt that return Boolean.
    #     title="ok cancel",
    #     message="Do you want to do that thing"):
    #     print('True')
    # else:
    #     print("False")
    # if messagebox.askretrycancel( # this show pop-up window with a prompt that return Boolean. It asks as a caution mark(Yellow CAUTION)
    #     title="ok cancel",
    #     message="Do you want to retry the thing"):
    #     print('True')
    # else:
    #     print("False")
    # if messagebox.askyesno( # this show pop-up window with a prompt that return Boolean.
    #     title="Ask Yes or No",
    #     message="Do you Like ...."):
    #     print('True')
    # else:
    #     print("False")
    # answer = messagebox.askquestion( # this show pop-up window with a prompt that return String (yes or no).
    #     title="Ask Question",
    #     message="Do you Like Pie")
    # if answer == 'yes':
    #     print(True)
    # else:
    #     print(False)
    
    answer = messagebox.askyesnocancel( # this show pop-up window with a prompt that return Boolean and On cancel A NONE value.
    title="Ask Yes No Cancel",
    message="Do you like to code",
    icon = 'warning') # this can change the default icon to the warning, It's an pre-defined term (info,warning,error).
    if answer == True:
        print("You Hit Yes Button")
    elif answer == False:
        print("You Hit No Button")
    elif answer == None:
        print("You Pressed Cancel Button")

window = Tk()

button = Button(window,
command = click,
text = "Click Me.")

button.pack()


window.mainloop()
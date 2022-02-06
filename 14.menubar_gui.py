from tkinter import *


# In this program we are going to create a menu bar (Drop Dowm menu-bar) on the screen of our root window or on the main window of the screen.

def openfile():
    print("File has been opened")
def savefile():
    print("FIle has been saved")
def cut():
    print("Cut function is inititated")
def copy():
    print("Copy function is inititated")
def paste():
    print("Paste function is inititated")


window = Tk()

openimage = PhotoImage(file="C:\\Users\\ASHISH\\Desktop\\Python GUI\\images\\open.png")
saveimage = PhotoImage(file="C:\\Users\\ASHISH\\Desktop\\Python GUI\\images\\save.png")
exitimage = PhotoImage(file="C:\\Users\\ASHISH\\Desktop\\Python GUI\\images\\stopsign.png")

# Menu is used to create the element menu bar or the root menu bar.
menubar = Menu( 
    window,)

# Here we configured the Menu to our root window.
window.config(menu=menubar)

filemenu = Menu( # here we create the menu of the menubar. Here the master window or the root window will be our menu bar.
    menubar,
    # Tearoff is to set the default (--) to null, after turning it to false by adding Zero it will be vanished from the screen. 
    tearoff=0,
    font=('MV Boli',8) 
    )

# Here the add_cascade is used to give the drop down effect of the menu. And we define the the label for which element.
menubar.add_cascade(label="File",menu=filemenu)

# This will put the inner commands or the function in the file menu. To make these menu function work we can add command and associate that to a function to do something.
filemenu.add_command(label="Open",command=openfile,image=openimage,compound='left') 
filemenu.add_command(label="Save",command=savefile,image=saveimage,compound='left' )

# This will seperate the inner menu from other inner menu by seperating them with a horizontal Ruler.
filemenu.add_separator()

# Here quit commnad is a pre-defined function so we don't have to create a function to initiate that.
filemenu.add_command(label="Exit",command=quit,image=exitimage,compound='left') 

editmenu = Menu(
    menubar,
    tearoff=0,
    font=("MV Boli",8),
    )
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="Paste",command=paste)

window.mainloop()
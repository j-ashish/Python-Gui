from tkinter import *

# Here we are going to move image.

def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-5)

def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+5)

def move_left(event):
    label.place(x=label.winfo_x()-5, y=label.winfo_y()) 

def move_right(event):
    label.place(x=label.winfo_x()+5, y=label.winfo_y())


window = Tk()
window.geometry("500x500")

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

racecar = PhotoImage(file=".\\images\\racecar.png")

label = Label(window,image=racecar)
label.place(x=3,y=0)







window.mainloop()
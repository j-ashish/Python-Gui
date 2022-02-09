# frame = a rectengular container to group and hold widgets.

from tkinter import *

window = Tk()
window.geometry('420x420')
frame = Frame(window,bg="pink",bd=5,relief=SUNKEN) #Frame is used to create an frame element. 
frame.place(x=0,y=0)

# The way to Create an empty button. In here we didn't add these element to root window, besides we put them inside the frame.
Button(frame,text="W",font=('Arial',25),width=3).pack(side=TOP) 
Button(frame,text="A",font=('Arial',25),width=3).pack(side=LEFT)
Button(frame,text="S",font=('Arial',25),width=3).pack(side=LEFT)
Button(frame,text="D",font=('Arial',25),width=3).pack(side=LEFT)

# Frame is just a constainer that contains element or widgets in it. It can be set at any position of the window.


window.mainloop()
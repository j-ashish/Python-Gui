from tkinter import *

# In this program we are going to drag and drop some items from our window to another co-ordinates by the mouse click and motion.

def drag_start(event): # Here we defined a function that is going to do the all heavy lifiting. If we put only the label name so we have to create another function associated with that element. So, here we provide a new variable that associates all widgets associated with that function and make it local for a function.
    labelcurrent = event.widget # Here we assign the value of the widgets in the variable.
    labelcurrent.startX = event.x # Here we assign the current x-axis co-ordinates to the variable.
    labelcurrent.startY = event.y # Here we assign the current y-axis co-ordinates to the variable.

# winfo_x or winfo_y is to get the current co-ordinates of the element
def drag_motion(event):
    labelcurrent = event.widget 
    x = labelcurrent.winfo_x() - labelcurrent.startX + event.x # Here we are getting the current value and adding the event occur value as a co-cordinates.
    y = labelcurrent.winfo_y() - labelcurrent.startY + event.y
    labelcurrent.place(x=x,y=y) # Here we are placing it to the current event occuring events.




window = Tk()

# We created labels that we can show on the screen that we are going to move.
label = Label(window,bg="red",width=10,height=5)
label.place(x=0,y=0)

label2 = Label(window,bg="red",width=10,height=5)
label2.place(x=100,y=100)

# We bind these labels to the event that are associated with some functions.
label.bind("<Button-1>",drag_start) # Here on click we pick or hold that value by there co-ordinates
label.bind("<B1-Motion>",drag_motion) # Here on motion our element is going to move along with the cursor to the new destination or to the new co-ordinates.

label2.bind("<Button-1>",drag_start) # Here on click we pick or hold that value by there co-ordinates
label2.bind("<B1-Motion>",drag_motion) # Here on motion our element is going to move along with the cursor to the new destination or to the new co-ordinates.



window.mainloop()
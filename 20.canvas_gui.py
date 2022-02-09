from tkinter import *



# canvas  = widget that is used to draw graphs, plots, images in a window.

window = Tk()

# Canvas is the fnction that binds the values and attributes to a variable.
canvas = Canvas(window,
height=500,
width=500)

# Create_line is a function that reside in the canvas element. It helps to create a straight line. To set-up a line you have to add some co-ordinates which are detrmined in axis's, as follows ({Start}x-axis,y-axis,{End}x-axis,y-axis)
# canvas.create_line(0,0,500,500,fill="blue",width=5) # Starting x&y-axis and ending x&y-axis
# canvas.create_line(0,500,500,0,fill="red",width=5) # Starting x&y-axis and ending x&y-axis

# create_rectangle is used to create rectangle shaped or square the diameter is depends on the co-ordinates we set same as above.
# canvas.create_rectangle(50,50,250,250,fill="purple")

#create_polygon is to create polygon type shape.
# canvas.create_polygon(250,0,500,500,0,500,fill="red",outline="black",width=5)

# In this example we define that we can set co-ordinates through a list and passing the list associated variable as co-ordinates.
# points = [250,0,500,500,0,500]
# canvas.create_polygon(points,fill="red",outline="black",width=5)

# There are different styles for this particular arc and start attribute can change the starting position of an arc (values must be in {degrees}). Extent expands the area of the arc.
# canvas.create_arc(0,0,500,500,fill="green",style=PIESLICE,start=90,extent=180)

canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
canvas.create_oval(190,190,310,310,fill="white",width=10)

canvas.pack()





window.mainloop()
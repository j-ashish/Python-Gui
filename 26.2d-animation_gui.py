from multiprocessing.context import SpawnContext
from tkinter import *
import time

# To create a constance we have to declare variables in all uppercase. So in future in won't change automatically.
WIDTH = 500
HEIGHT = 500
xvelocity = 3
yvelocity = 2

window = Tk()


canvas = Canvas(window,width=WIDTH,height=HEIGHT,)
canvas.pack()

spacebg = PhotoImage(file="C:\\Users\\ASHISH\\Desktop\\Python GUI\\images\\earth.png")
background = canvas.create_image(0,0,image=spacebg,anchor=NW)

ufo = PhotoImage(file=".\\images\\ufo.png")
my_image = canvas.create_image(0,0,image=ufo,anchor=NW)


image_width = ufo.width()
image_height = ufo.width()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if (coordinates[0] >= WIDTH - image_width) or (coordinates[0] < 0):
        xvelocity = -xvelocity
    if (coordinates[1] >= HEIGHT - image_width) or (coordinates[1] < 0):
        yvelocity = -yvelocity
    canvas.move(my_image,xvelocity,yvelocity)    
    window.update()
    time.sleep(0.01)


window.mainloop()
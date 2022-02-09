from tkinter import *
import time
from ball_27 import Ball

window = Tk()

HEIGHT = 500
WIDTH = 500



canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

# def __init__(self,canvas,x,y,diameter,xvelocity,yvelocity,color):

volley_ball = Ball(canvas,0,0,100,1,2,"white")
tennis_ball = Ball(canvas,0,0,100,4,3,"yellow")
basket_ball = Ball(canvas,0,0,120,8,7,"orange")

while True:
    volley_ball.mo()
    tennis_ball.mo()
    basket_ball.mo()
    window.update()
    time.sleep(0.0001)

window.mainloop()



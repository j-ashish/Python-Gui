
from tkinter import *

def submit():
    print(f'the temprature is {scale.get()} C')


window = Tk()

hot = PhotoImage(file=".\\images\\hot.png")
cold = PhotoImage(file=".\\images\\cold.png")

hotlabel = Label(image=hot)
hotlabel.pack()
scale = Scale(window,
from_= 0,
to = 100,
length = 600,
width= 50,
orient=VERTICAL,
font = ("Comic Sans",20),
tickinterval=10, # this adds numeric indicators for values.
showvalue = 1,  # showvalue 0 for false and 1 for true.
resolution=5, # increament of a slider 
troughcolor="#69EAFF", # troughcolor is to change the color of the sliderbar background.
fg = "#FF1C00",
bg = "Black",

)
scale.set( ((scale['from'] - scale['to']) / 2) + scale['to'] )  # this is used to make the default to the middle of the value, whatever the value will be, the placeholder will always be in the middle.
# scale.set(20) # this is like a placeholder, but this indicates the default value and pre-select the value which we have passed as a parameter.
scale.pack()
coldlabel = Label(image=cold)
coldlabel.pack()
#----------------------

button = Button(window,
text = "submit",
command = submit
)
button.pack()


window.mainloop()
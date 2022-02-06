from tkinter import *

# radiobutton.

food = ["pizza","hamburger","hotdog"]

def order(): # in this function the variable will pass a value if the value matches the given task will be initiated.
    if(x.get()==0):
        print("You ordered pizza!") 
    elif(x.get()==1):
        print("You ordered a hamburger!")
    elif(x.get()==2):
        print("You ordered a hotdog!")
    else:
        print("huh?")

window = Tk()

pizzaImage = PhotoImage(file='.\\images\\pizza.png')
hamburgerImage = PhotoImage(file='.\\images\\hamburger.png')
hotdogImage = PhotoImage(file='.\\images\\hotdog.png')
foodImages = [pizzaImage,hamburgerImage,hotdogImage]

x = IntVar()

for index in range(len(food)):  # for loop to access every value in the list.
    radiobutton = Radiobutton(window,
                              text=food[index], #adds text to radio buttons
                              variable=x, #groups radiobuttons together if they share the same variable
                              value=index, #assigns each radiobutton a different value
                              padx = 25, #adds padding on x-axis
                              font=("Impact",50),
                              image = foodImages[index], #adds image to radiobutton
                              compound = 'left', #adds image & text (left-side)
                              #indicatoron=0, #eliminate circle indicators
                              #width = 375, #sets width of radio buttons
                              command=order #set command of radiobutton to function
                              )
    radiobutton.pack(anchor=W) # anchor is used to instruct for the position on the screen. The value are in Directions N - north NE - North Easr and so on so forth.
window.mainloop()
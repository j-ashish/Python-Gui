from tkinter import *

# label = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file='.\\images\\foodbar.png')

label = Label(window, # Label is used to create a label for a Gui window.
              text="bro, do you even code?", # the text here put the text on the label.
              font=('Arial',40,'bold'), # font is to set the size and the style of the content.
              fg='#00FF00', # foreground color text color
              bg='black', # background color, color of the element.
              relief=RAISED,
              bd=10, # bd is used to set the border around the element. Values detrmine to put border are in Pixels.
              padx=20, # it is used to add padding at the x-axis in pixels
              pady=20, # it is used to add padding at the y-axis in pixels
              image=photo, # it adds the image all over the element, and even covers the label text. To iradicate this disadvantage we have to use the method given below.
              compound='bottom') # this mehtod enables image to be on the element but it sets the position and put aside with any other configuration.
label.pack()
#label.place(x=0,y=0) # label place is used to put the element on the screen according to the x and y axis.

window.mainloop()
from tkinter import *

window = Tk() #instantiate an instance of a window
window.geometry("420x420") # Geometry function is used to set the minimu height and width of the Gui window or interface.
window.title("Bro Code first GUI program") # this indicate the heading of the program.

icon = PhotoImage(file='.\\images\\foodbar.png') # photo image function is used to turn the png format file to a python accepted format. To change it to that format we have to enter the path in the file attribute.z
window.iconphoto(True,icon) # here is the function that set the default feather title photo or icon to user detrmined icon.
window.config(background="#5cfcff") # config is used to configure some setting of the interface.

window.mainloop() #place window on computer screen, listen for events
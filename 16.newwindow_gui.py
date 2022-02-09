from tkinter import *

# Toplevel() top level window = New window 'on top' of the other windows, linked to a 'bottom' window. If the bottom window is closed so the associated bottom window will be closed. They are stacked to the bottom window. 
# Tk() main window = This window is not associated with any other window, it is own is own. If we drop the Top window so it doesn't effect the bottom window. New independent window.

def create_window():
    new_window = Tk()

    # This destroy method will close or destroy the window associated with this variable.
    old_window.destroy() 
old_window = Tk()

# Here on the click on the button our old window will be demolished and the new window will generate.
Button(old_window,text="Create New Window",command=create_window).pack() 


old_window.mainloop()
from tkinter import *

def dosomething(event):
    print("You did A thing")
    
    # This will print the co-ordinates of the click, at which area of the window mouse click occured.
    print(event.x,event.y) 

window = Tk()


# Mouse events are the same as the key events. But the values are little bit different.
# window.bind("<Button-1>",dosomething)  # Button-1 is associated with Left Mouse Click. Button-2 is associated with Scroll and it triggers on click not on scrolling. Button-3 is associated with the right mouse click.

# It will be triggered when user release the click.
# window.bind("<ButtonRelease>",dosomething)

# It will trigger when user's mouse enters window.
# window.bind("<Enter>",dosomething)

# It will trigger when user mouse leaves the window.
window.bind("<Leave>",dosomething)

# It will trigger only when the mouse is in the movement.
window.bind("<Leave>",dosomething)


 
window.mainloop()
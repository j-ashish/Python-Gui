from tkinter import *
from tkinter.ttk import *
from tkinter.ttk import Style
import time

# In this program we are going to define how to create the progress bar.

def start():
    tasks = 100
    x = 0
    while x < tasks:
        time.sleep(0.05)
        bar['value']+=1 # Value is the pre-defined attribute for the widget holding variable.
        x+=1
        percent.set(str(int((x/tasks)*100))+"%")
        text.set(str(x)+"/"+str(tasks)+" Tasks Completed")
        window.update_idletasks()


window = Tk()

# We assign these two variables as string to get the value from the function an use them in our bars..
percent = StringVar()
text = StringVar()

# s = Style()
# s.theme_use('clam')
# s.configure("red.Horizontal.TProgressbar",foreground='blue',background='blue')

bar = Progressbar(window, # Progressbar is used to create the progress bar.
orient=HORIZONTAL,
length=300,
# style="red.Horizontal.TProgressbar"
)
bar.pack(pady=10)

percentlabel = Label(window,
textvariable= percent # here we used textvariable so we can update the variable value.
).pack()

tasklabel = Label(window,
textvariable= text # here we used textvariable so we can update the variable value.
).pack()

button = Button(window,
text = "Download",
command = start).pack()



window.mainloop()
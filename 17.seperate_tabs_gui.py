from tkinter import *
from tkinter.ttk import Notebook


window = Tk()

# This Notebook widgets manages the collections of windows and displays.
notebook = Notebook(window)

# New frame for a Tab 1
tab1 = Frame(notebook) 
tab2 = Frame(notebook) 

# Here we added our frames in the notebook and later we associate these tab with the label given below.
notebook.add(tab1,text="Tab 1")
notebook.add(tab2,text="Tab 2")

# Expand= expand yo fill any space not otherwise used. Fill = This will fill space on X and Y axis. (both is for both side, but we can put x or y delebirately.)
notebook.pack(expand=True,fill="both") 

# Here we assigned or associate these label to our notebook or the other window.
Label(tab1,text="Hello, This is Tab no.1",width=50,height=25,bd=10,relief=RAISED).pack(anchor=NW)
Label(tab2,text="Hello again, This is Tab no.2",width=50,height=25).pack()
window.mainloop()
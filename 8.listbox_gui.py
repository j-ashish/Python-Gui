from tkinter import *


def submit():
    food = []
    for i in listbox.curselection(): # curselection is function to get the current selected value of a lsitbox. In here we add the multiple value in the listbox but it can't handle multiple values on it's own. So, we add the list to get all the values of the current selection or selections.
        food.insert(i,listbox.get(i))
    
    print("You have Ordered:- ")
    for j in food:
        print(j)


def add():
    listbox.insert(listbox.size() + 1, entrybox.get()) # here insert fucntion take the total numbers + 1 as new index and the entry get for the new value we entered.
    listbox.config(height=listbox.size()) # and later on to set the list on the size according to the content we put the same function as we put below.


def delete():
    for i in reversed(listbox.curselection()): # same it can't delete the selection all at once, so here we added a loop. But adding a loop doesn't work because the index value will change upon deletion so we have to put the reversed function to work when the index changed.
        listbox.delete(i)

# Creating list box in Gui, Tkinter Framework.
# Listbox = A listing of selectable text items within it's own container.


window = Tk()


listbox = Listbox(window, # Listbox is used to create a listbox.
bg="#f7ffde",
font=("Constantia", 20), 
width=12,
selectmode=MULTIPLE) # selectmode is used to select more than one option in a selectbox.

listbox.pack()
listbox.insert(1, "Pizza") # insert function is used to add the options or the items in a listbox.
listbox.insert(2, "Pasta") # Syntax = (index,'item')
listbox.insert(3, "Garlic Bread")
listbox.insert(4, "Soup")
listbox.insert(5, "Salad")


listbox.config(height=listbox.size()) # here height is configured according to the items in it.

entrybox = Entry(window)
entrybox.pack()


submit_button = Button(window, text="Submit", command=submit,) # here submit function is used to tell that how much item you have selected.
submit_button.pack()

add_button = Button(window, text="Add", command=add,) # add button here will add the item in a list by adding the item name in the entry box and pressing the add button.
add_button.pack()

del_button = Button(window,text="Delete",command=delete,) # here delete button will iradicate the items from the list upon selection and press this button.

del_button.pack()


window.mainloop()

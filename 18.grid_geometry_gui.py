from tkinter import *


# grid()  = geometry manager that organizes widgets in a table-like structure in a parents. It's same like pack but it is more flexible when it comes to setting up.

"""
Example of rows and columns:-
            column_1    column_2    column_3    column_4    ...........
                0           1           2           3
row_1    0 _____|___________|___________|___________|   
                |           |           |           |
row_2    1 _____|___________|___________|___________|   
                |           |           |           |    
row_3    2 _____|___________|___________|___________|   

.
.
.
"""


window = Tk()

titlelabel = Label(window, text="Enter Your Info", font=(
    "Arial", 20)).grid(row=0, column=0, columnspan=2)


# In grid we can define at which position we want to see our element, to define the position we can define it in Rows and Columns, rows and columns are defined by indexing which starts from 0. In colspan it takes the position in between 2 element and takes the both position width.
firstname_label = Label(window, text="First Name: ",
                        width=20, bg="red").grid(row=1, column=0) 
firstname_entry = Entry(window).grid(row=1, column=1)

# If the element width is not defined so the default width of the elemets are set to the biggest element.
lastname_label = Label(window, text="Last Name: ",
                       width=25, bg="Green").grid(row=2, column=0)
lastname_entry = Entry(window).grid(row=2, column=1)

email_label = Label(window, text="E-mail: ", width=15,
                    bg="blue").grid(row=3, column=0)
email_entry = Entry(window).grid(row=3, column=1)

submit = Button(window,
                text="Submit",
                ).grid(row=3, column=0, columnspan=2)  # columnspan is used to state the element to take the half of the column determine and half of the column brfore the selected column

window.mainloop()

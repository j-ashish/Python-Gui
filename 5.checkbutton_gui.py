from tkinter import *

def display():
    if(x.get()==1): # here this function is getting the value on the execution, if the value matched the if clause will run otherwise the else will be activated.
        print("You agree!")
    else:
        print("You don't agree :(")

window = Tk()

x = IntVar() # the variable is declared before entring the element and assigned as Int because the value we are retriving is integer. If the value is Boolean so we have to use - BooleanVar() or for string StrVar().

python_photo = PhotoImage(file='.\\images\\foodbar.png')

check_button = Checkbutton(window, # checkbutton is the function that allows to create a button that is get checked when clicked.
                           text="I agree to something", # text to show text along with the button.
                           variable=x, # it assigns the variable to the element for getting the value.
                           onvalue=1, # onvalue is used to assign value to the variable when it is active or clicked. It can be Bool,Int,Str.
                           offvalue=0, # offvalue assigned when the situation is opposite, when the button isn't clicked.
                           command=display, # function assigned to when the activation occurs.
                           font=('Arial',20),
                           fg='#00FF00',
                           bg='black',
                           activeforeground='#00FF00',
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=python_photo,
                           compound='left')
check_button.pack()


window.mainloop()
from tkinter import *

def Result():
 
    # Sub Window
    sub = Toplevel()
    sub.title("Result")
    sub_text = Label(sub, text = 'Your Height is: ' )
    sub_text.pack()
    sub.geometry("300x100")

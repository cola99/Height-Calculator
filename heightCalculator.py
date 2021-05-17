
from tkinter import * 
from mathcalc import *  

def MainWindow():
    root = Tk()       
    root.title("Most Advanced Calculator")      
    root.geometry('500x200')

    # Top Text
    top_text = Label (root, text = 'Enter your height in: cm.')
    top_text.pack(side = 'top', padx = '10', pady = '10')

    # Input
    input_box = Entry(root)
    input_box.pack()

    # Button
    calculate_button = Button(root, text = 'Calculate', bd = '3', padx = '10', pady = '10', command = root.destroy)
    calculate_button.pack(side = 'bottom', padx = '20', pady = '20')   
    
    root.mainloop()

MainWindow()
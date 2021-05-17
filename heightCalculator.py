# Libs
from tkinter import *
from result import *
from mathstuff import *

def MainWindow():
    root = Tk()       
    root.title("Most Advanced Calculator")      
    root.geometry('300x150')

    # Top Text
    top_text = Label (root, text = 'Enter your height in: cm.')
    top_text.pack(side = 'top', padx = '10', pady = '10')

    # Insane Math/Calculation
    MathStuff()

    # Button
    calculate_button = Button(root, text = 'Calculate', bd = '3', padx = '10', pady = '10', command = Result)
    calculate_button.pack(side = 'bottom', padx = '20', pady = '20')   
    

    root.mainloop()

MainWindow()



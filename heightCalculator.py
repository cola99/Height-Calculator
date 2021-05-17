
from tkinter import *   

def MainWindow():
    root = Tk()       
    root.title("Most Advanced Calculator")      
    root.geometry('500x200')

    top_text = Label (root, text = 'Guwno w gaciah')

    top_text.pack(side = 'top', padx = '10', pady = '10')


    calculate_button = Button(root, text = 'Calculate', bd = '3', padx = '10', pady = '10', command = root.destroy)
    

    calculate_button.pack(side = 'bottom', padx = '20', pady = '20')   
    
    root.mainloop()
    
MainWindow()
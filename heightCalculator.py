from tkinter import * # Tk

root = Tk()       
root.title("Most Advanced Calculator")      
root.geometry('550x100')
root.resizable(False, False)

# Labels
label_1 = Label(root, text="Enter your height:")
label_1.grid(column=0, row=0, padx=15, pady=30)

# Entrys
entry_1 = Entry(root, width=50)
entry_1.grid(column=1, row=0, padx=15, pady=5)
  
# Buttons
button1 = Button(root, text="Calculate")
button1.grid(column=2, row=0, padx=15, pady=5)

root.mainloop()





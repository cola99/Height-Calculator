from tkinter import * # Tk
 
 # Window
root = Tk()
root.title('Height Calculator')
root.geometry("400x200")
root.resizable(False, False)
 
def returnEntry():
    result = myEntry.get()
    resultLabel.config(text="Your Height is roughly: " + result + "cm")
 
# Label
topLabl = Label(root,text="Enter Your Height: ")
topLabl.grid(column=0, row=0, padx=20, pady=30)

# Entry
myEntry = Entry(root, width=20)
myEntry.bind("<Return>",returnEntry)
myEntry.grid(column=1, row=0, padx=20, pady=30)
 
# Button
enterEntry = Button(root, text= "Calculate", command=returnEntry)
enterEntry.grid(column=2, row=0, padx=20, pady=30)
 
# Emplty Label
resultLabel = Label(root, text = "")
resultLabel.grid()


root.mainloop()
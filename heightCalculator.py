# Display Entry in a Label
 
from tkinter import * 
 
root = Tk()
 
def returnEntry(arg=None):
    """Gets the result from Entry and return it to the Label"""
 
    result = myEntry.get()
    resultLabel.config(text=result)
    myEntry.delete(0,END)
 
# Create the Entry widget
myEntry = Entry(root, width=20)
myEntry.bind("<Return>",returnEntry)
myEntry.grid(column=0, row=0, padx=15, pady=30)
 
# Create the Enter button
enterEntry = Button(root, text= "Calculate", command=returnEntry)
enterEntry.grid(column=2, row=0, padx=15, pady=30)
 
# Create and emplty Label to put the result in
resultLabel = Label(root, text = "")
resultLabel.grid(column=3, row=0, padx=15, pady=30)
 
 
root.geometry("550x100")
 
root.mainloop()
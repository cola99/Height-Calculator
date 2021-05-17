from tkinter import * # Tk
 
 # Window
root = Tk()
root.title('Height Calculator')
root.geometry("300x100")
root.resizable(False, False)
 
def returnEntry():
    result = myEntry.get()
    resultLabel.config(text="Your Height is roughly: " + result + "cm")
 
# Label
topLabl = Label(root,text="Enter Your Height: (cm) ")
topLabl.pack()

# Entry
myEntry = Entry(root, width=20)
myEntry.pack()
 
# Button
enterEntry = Button(root, text= "Calculate", command=returnEntry)
enterEntry.pack(pady=5)
 
# Emplty Label
resultLabel = Label(root, text = "")
resultLabel.pack()


root.mainloop()
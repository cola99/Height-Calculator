import tkinter

root = tkinter.Tk()
root.title("Most Advanced Calculator")

label_result = tkinter.Label(root, text="")
label_result.grid(row=0, column=0)

button_1 = tkinter.Button(root, text="1", command=add())
button_1.grid(row=1, column=0)

button_2 = tkinter.Button(root, text="2", command=add())
button_2.grid(row=1, column=0)

root.mainloop()
from tkinter import *
root = Tk()
root.geometry("300x500")

frame = Frame(root)
frame.pack()
Var1 = IntVar()
ChkBttn = Checkbutton(frame, width = 15, variable = Var1)
ChkBttn.pack(padx = 5, pady = 5)

root.mainloop()
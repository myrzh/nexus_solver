from tkinter import *
root = Tk()
root.geometry("1280x720")

frame = Frame(root)
frame.pack()
Var1 = IntVar()
ChkBttn = Checkbutton(frame, width = 15, variable = Var1)
ChkBttn.pack(padx = 5, pady = 5)

root.mainloop()
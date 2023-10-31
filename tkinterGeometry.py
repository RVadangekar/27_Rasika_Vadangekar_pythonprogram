from tkinter.colorchooser import askcolor
from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox
top = Tk()

top.geometry("100x100")
def show():
   color = askcolor()
   print(color)
   num = askinteger("Input", "Input an Integer")
   print(num)
   
B = Button(top, text ="Click", command = show)
B.place(x=50,y=50)

top.mainloop()

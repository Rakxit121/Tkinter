from tkinter import *

root = Tk()

e1=Entry(root, width=50,fg="blue",bg="white")
e1.pack()
def myClick():
    mylabel = Label(root, text="Welcome to Tkinter "+e1.get(),width=50,fg="green",bg="white")
    mylabel.pack()

myButton=Button(root, text="Click Me", command= myClick, fg="white", bg="grey")
myButton.pack()



root.mainloop()

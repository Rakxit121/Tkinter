from tkinter import *

root = Tk()
root.geometry("300x200")

# Text
hello = Label(root, text=" Hello World!!")
hello.place(x=110, y= 10)  # saves data as print

# Rows and column of place
name = Label(root, text="Name")
name.place(x=30, y=50)
Entry(root).place(x=100, y=50)

password = Label(root, text="Password")
password.place(x=30, y=90)
Entry(root).place(x=100, y=90)
# Button
Button(root, text="Login", fg="green").place(x=150, y=120)

# Button
Button(root, text="Register", fg="red").place(x=145, y=160)

root.mainloop()

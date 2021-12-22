from tkinter import *

root = Tk()
root.geometry("300x200")

# Text
hello = Label(root, text=" Hello World!!")
hello.pack(side=TOP)  # saves data as print

# Rows and column of pack
name = Label(root, text="Name")
name.pack()
Entry(root).pack()

password = Label(root, text="Password")
password.pack()
Entry(root).pack()
# Button
Button(root, text="Login", fg="green").pack()

# Button
Button(root, text="Register", fg="red").pack()

root.mainloop()

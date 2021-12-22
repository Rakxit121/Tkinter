from tkinter import *

root = Tk()
# Text
hello = Label(root, text=" Hello World!!")
hello.grid()  # saves data as print

# Rows and column of grid
name = Label(root, text="Name")
name.grid(row=2, column=2)
ent1 = Entry(root).grid(row=2, column=3)

password = Label(root, text="Password")
password.grid(row=3, column=2)
ent2 = Entry(root).grid(row=3, column=3)
# Button
Button(root, text="Register", fg="Blue").grid(row=4, column=2)

# Button
Button(root, text="Register", fg="red").grid(row=6, column=3)

root.mainloop()

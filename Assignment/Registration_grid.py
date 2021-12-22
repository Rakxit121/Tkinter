# WAP to make tkinter registration form with grid() containing::
# First name, Last name, Email, password, Confirm registration

from tkinter import *

root = Tk()
root.geometry("600x400")

registration = Label(root, text=" Registration Form:")
registration.grid(row=2, column=7)

F_name = Label(root, text="First Name:")
F_name.grid(row=4, column=6)
Entry(root).grid(row=4, column=7)

L_name = Label(root, text="Last Name:")
L_name.grid(row=6, column=6)
Entry(root).grid(row=6, column=7)

Email = Label(root, text="Email:")
Email.grid(row=8, column=6)
Entry(root).grid(row=8, column=7)

password = Label(root, text="Password:", fg="green")
password.grid(row=10, column=6)
Entry(root).grid(row=10, column=7)

c_password = Label(root, text="Confirm Password:", fg="green")
c_password.grid(row=12, column=6)
Entry(root).grid(row=12, column=7)

Button(root, text="Login", fg="green").grid(row=14, column=7)


Button(root, text="Cancel", fg="red").grid(row=14, column=8)

root.mainloop()

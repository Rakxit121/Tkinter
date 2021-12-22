# WAP to make tkinter registration form with pack() containing::
# First name, Last name, Email, password, Confirm registration

from tkinter import *

root = Tk()
root.geometry("600x400")

registration = Label(root, text=" Registration Form:")
registration.pack()


F_name = Label(root, text="First Name:")
F_name.pack()
Entry(root).pack()

L_name = Label(root, text="Last Name:")
L_name.pack()
Entry(root).pack()

Email = Label(root, text="Email:")
Email.pack()
Entry(root).pack()

password = Label(root, text="Password:", fg="green")
password.pack()
Entry(root).pack()

c_password = Label(root, text="Confirm Password:", fg="green")
c_password.pack()
Entry(root).pack()

Button(root, text="Login", fg="green").pack()
Button(root, text="Cancel", fg="red").pack()

root.mainloop()

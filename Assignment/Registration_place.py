# WAP to make tkinter registration form with place() containing::
# First name, Last name, Email, password, Confirm registration

from tkinter import *

root = Tk()
root.geometry("600x400")

registration = Label(root, text=" Registration Form:")
registration.place(x=220, y=10) 

F_name = Label(root, text="First Name:")
F_name.place(x=50, y=60)
Entry(root).place(x=170, y=60)

L_name = Label(root, text="Last Name:")
L_name.place(x=50, y=90)
Entry(root).place(x=170, y=90)

Email = Label(root, text="Email:")
Email.place(x=50, y=120)
Entry(root).place(x=170, y=120)

password = Label(root, text="Password:", fg="green")
password.place(x=50, y=150)
Entry(root).place(x=170, y=150)

c_password = Label(root, text="Confirm Password:", fg="green")
c_password.place(x=50, y=180)
Entry(root).place(x=170, y=180)
# Button
Button(root, text="Login", fg="green").place(x=170, y=210)

# Button
Button(root, text="Cancel", fg="red").place(x=250, y=210)

root.mainloop()

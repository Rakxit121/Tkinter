# Login form with grid() containing:

from tkinter import *

root = Tk()
root.geometry("300x300")

Label(root, text=" Log In to Your Account", font="16").grid(row=2, column=4)

Label(root, text="Email:").grid(row=5, column=4)
entry1 = Entry(root, width=25)
entry1.grid(row=7, column=4)

Label(root, text="Password:", fg="green").grid(row=9, column=4)
entry2 = Entry(root, width=25)
entry2.grid(row=11, column=4)

Label(root, text="").grid(row=12, column=4)

forgot = Button(root, text=" Forgot your password?", fg="blue", height=1, width=35)
forgot.grid(row=13, column=4)
Label(root, text="").grid(row=14, column=4)
Button(root, text="Log In", fg="light blue", bg="Blue",height=2,width=25).grid(row=15, column=4)
Label(root, text="").grid(row=16, column=4)
Button(root, text="Sign up", fg="blue").grid(row=17, column=4)

root.mainloop()

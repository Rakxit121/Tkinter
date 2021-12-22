# Login form with pack() containing:


from tkinter import *

root = Tk()
root.geometry("400x400")

Label(root, text=" Log In to Your Account", font="16").pack()

Label(root, text="").pack()
Label(root, text="Email:", justify="left").pack()
entry1 = Entry(root, width=25)
entry1.pack()

Label(root, text="Password:", fg="green").pack()
entry2 = Entry(root, width=25)
entry2.pack()

Label(root, text="").pack()

forgot = Button(root, text=" Forgot your password?", fg="blue", height=1, width=35)
forgot.pack()
Label(root, text="").pack()
Button(root, text="Log In", fg="White", bg="Blue",height=2, width=15,font=12).pack()
Label(root, text="").pack()
Button(root, text="Sign up", fg="blue").pack()

root.mainloop()

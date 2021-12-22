# Login form with place() containing:


from tkinter import *

root = Tk()
root.geometry("500x400")

Label(root, text=" Log In to Your Account", font="16").place(x=150, y=20)

Label(root, text="").place()
Label(root, text="Email:", font=11).place(x=30, y=90)
entry1 = Entry(root, width=30, )
entry1.place(x=140, y=90, height=30)

Label(root, text="Password:", font=5).place(x=30, y=130)
entry2 = Entry(root, width=30)
entry2.place(x=140, y=130, height=30)

forgot = Button(root, text=" Forgot your password?", fg="blue", height=1, width=35)
forgot.place(x=180, y=165)
Label(root, text="").place()
Button(root, text="Log In", fg="White", bg="light blue", height=2, width=8, font=12).place(x=150, y=200)

Button(root, text="Sign up", fg="cyan").place(x=170, y=270)

root.mainloop()

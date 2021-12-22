from tkinter import *

root = Tk()
root.title("Bill Print using place in tkinter")
root.geometry("1000x600")

var1 = IntVar()
Checkbutton(root, text="Room Charge", variable=var1).place(x=10, y=50)

var2 = IntVar()
Checkbutton(root, text="Food", variable=var2).place(x=10, y=80)

var3 = IntVar()
Checkbutton(root, text="Service", variable=var3).place(x=10, y=110)

var4 = IntVar()
Checkbutton(root, text="Extra", variable=var4).place(x=10, y=140)

var5 = IntVar()
Checkbutton(root, text="Tax", variable=var5).place(x=10, y=170)
Label(root, text="Total").place(x=600, y=10)

e1 = Entry(root)
e1.place(x=140, y=50)

e2 = Entry(root)
e2.place(x=140, y=80)

e3 = Entry(root)
e3.place(x=140, y=110)

e4 = Entry(root)
e4.place(x=140, y=140)

e5 = Entry(root)
e5.place(x=140, y=170)

e6 = Entry(root)
e6.place(x=300, y=50)

e7 = Entry(root)
e7.place(x=300, y=80)

e8 = Entry(root)
e8.place(x=300, y=110)

e9 = Entry(root)
e9.place(x=300, y=140)

e10 = Entry(root)
e10.place(x=300, y=170)

tot = Label(root, text="", font="arial 22 bold")
tot.place(x=650, y=10)

Button(root, text="Add", height=3, width=13).place(x=10, y=220)

Button(root, text="Print", command=print, height=3, width=13).place(x=850, y=120)
cols = ('item', 'price', 'qty', 'total')



root.mainloop()
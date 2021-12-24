from tkinter import *

root = Tk()

breadth = Label(root, text="Input breadth for area of triangle ", width=50, fg="red", bg="white")
breadth.pack()
e1 = Entry(root, width=10, fg="blue", bg="white")
e1.pack()
length = Label(root, text="Input length for area of triangle ", width=50, fg="red", bg="white")
length.pack()
e2 = Entry(root, width=10, fg="blue", bg="white")
e2.pack()


def area():

    l = float(e1.get())
    b = float(e2.get())
    triangle = float((1/2)*(l*b))
    triangle_str = str(triangle)

    area_of = Label(root, text="area of triangle = (1/2)x(" + e1.get()+"x" + e2.get()+")", width=50, fg="green", bg="white", font=11)
    area_of.pack()
    ans = Label(root, text=" = " + triangle_str, width=50, fg="green", bg="white", font=11)
    ans.pack()


myButton = Button(root, text="Calculate", command=area, fg="white", bg="grey")
myButton.pack()

root.mainloop()

from tkinter import *

root = Tk()

area_circle = Label(root, text="Input radius for area of circle ", width=50, fg="red", bg="white")
area_circle.pack()
e1 = Entry(root, width=50, fg="blue", bg="white")
e1.pack()


def area():
    a = 0
    b = ""
    pi = 22 / 7
    R = (e1.get())
    r = float(R)
    circle = pi * (r ** 2)
    circle_str = str(circle)
    if len(circle_str) > 6:
        while len(b) != 6:
            for i in range(1, 7):
                a = a + int(circle[i])
            b = str(a)
    circle_str = a

    area_of = Label(root, text="area of circle = pi*(" + e1.get() + "^2)", width=50, fg="green", bg="white", font=11)
    area_of.pack()
    ans = Label(root, text=" = " + circle_str, width=50, fg="green", bg="white", font=11)
    ans.pack()


myButton = Button(root, text="Calculate", command=area, fg="white", bg="grey")
myButton.pack()

root.mainloop()

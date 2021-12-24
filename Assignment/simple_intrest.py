from tkinter import *

root = Tk()

root.geometry("600x400")

Label(root, text="Principle : ").place(x=5, y=5)

principle_input = Entry(root, width=15)
principle_input.place(x=75, y=5)

Label(root, text="Time : ").place(x=5, y=35)

time_input = Entry(root, width=15)
time_input.place(x=75, y=35)

Label(root, text="Rate : ").place(x=5, y=70)

rate_input = Entry(root, width=15)
rate_input.place(x=75, y=70)


def si():
    """Stored Value of Principle,rate & TIme in p,r&t respectively"""
    p = int(principle_input.get())
    t = int(time_input.get())
    r = int(rate_input.get())
    simple = (p * t * r) / 100
    output = "Simple Interest : " + str(simple)
    Label(root, text=output).place(x=65, y=130)


Button(root, text="Simple Interest", padx=3, pady=3, command=si).place(x=45, y=100)

root.mainloop()

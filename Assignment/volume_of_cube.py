from tkinter import *

Volume = Tk()
Volume.geometry("600x400")

Label(Volume, text="Enter Edge of cube:").place(x=0, y=0)
edg_input = Entry(Volume, width=10)
edg_input.place(x=130, y=0)


def volume():
    e = float(edg_input.get())
    v = e * e * e
    vo = "Volume of Cube is : " + str(v)
    Label(Volume, text=str(vo)).place(x=55, y=110)


Button(Volume, text="Volume", padx=5, pady=5, command=volume).place(x=50, y=40)
Volume.mainloop()

from tkinter import *

BMI = Tk()
BMI.geometry("600x400")
Label(BMI, text="Enter Mass of Person:").place(x=0, y=0)
rad_input = Entry(BMI, width=10)
rad_input.place(x=130, y=0)
Label(BMI, text="Enter Height of Person:").place(x=0, y=30)
rad2_input = Entry(BMI, width=10)
rad2_input.place(x=130, y=30)


def area():
    m = float(rad_input.get())
    h = float(rad2_input.get())
    a = m / (h * h)
    ar = "BMI of Person is : " + str(a)
    Label(BMI, text=str(ar)).place(x=55, y=110)


Button(BMI, text="Area", padx=5, pady=5, command=area).place(x=50, y=70)

BMI.mainloop()

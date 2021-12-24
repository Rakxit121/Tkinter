# Simple Arithmetic Calculator using grid method

from tkinter import *

root = Tk()
root.geometry("355x270")

calc = Label(root, text="Standard Calculator")
calc.grid(row=1, column=1)
Entry(root).grid(row=1, column=3)

button1 = Button(root, text=' 1 ', fg='black', bg='white', height=2, width=7, command=lambda: button_click(1))
button1.grid(row=3, column=0)

button2 = Button(root, text=' 2 ', fg='black', bg='white', height=2, width=7, command=lambda: button_click(2))
button2.grid(row=3, column=1)

button3 = Button(root, text=' 3 ', fg='black', bg='white', height=2, width=7, command=lambda: button_click(3))
button3.grid(row=3, column=2)

button4 = Button(root, text=' 4 ', fg='black', bg='white', height=2, width=7, command=lambda: button_click(4))
button4.grid(row=4, column=0)

button5 = Button(root, text=' 5 ', fg='black', bg='white', height=2, width=7, command=lambda: button_click(5))
button5.grid(row=4, column=1)

button6 = Button(root, text=' 6 ', fg='black', bg='white', height=2, width=7, command=lambda: button_click(6))
button6.grid(row=4, column=2)

button7 = Button(root, text=' 7 ', fg='black', bg='white', height=2, width=7, command=lambda: button_click(7))
button7.grid(row=5, column=0)

button8 = Button(root, text=' 8 ', fg='black', bg='white', height=2, width=7, command=lambda: button_click(8))
button8.grid(row=5, column=1)

button9 = Button(root, text=' 9 ', fg='black', bg='white', height=2, width=7, command=lambda: button_click(9))
button9.grid(row=5, column=2)

button0 = Button(root, text=' 0 ', fg='black', bg='white', height=2, width=7, command=lambda: button_click(0))
button0.grid(row=6, column=0)

plus = Button(root, text=' + ', fg='black', bg='white', height=2, width=7, command=lambda: button_plus)
plus.grid(row=3, column=3)

minus = Button(root, text=' - ', fg='black', bg='white', height=2, width=7, command=lambda: button_minus)
minus.grid(row=4, column=3)

multiply = Button(root, text=' * ', fg='black', bg='white', height=2, width=7)
multiply.grid(row=5, column=3)

divide = Button(root, text=' / ', fg='black', bg='white', height=2, width=7)
divide.grid(row=6, column=3)

equal = Button(root, text=' = ', fg='black', bg='white', height=2, width=7)
equal.grid(row=6, column=2)

clear = Button(root, text='Clear', fg='black', bg='white', height=2, width=7)
clear.grid(row=6, column=1)

Decimal = Button(root, text='.', fg='black', bg='white', height=2, width=7)
Decimal.grid(row=7, column=0)

root.mainloop()

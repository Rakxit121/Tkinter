from tkinter import *
from PIL import ImageTk, Image


def forward(img):
    global label
    global button_forward
    global button_back
    global button_exit
    label.grid_forget()

    #  clearing the screen so that our next image can pop up
    label = Label(image=List_images[img-1])
    # as the list starts from 0, so we are subtracting one
    label.grid(row=1, column=0, columnspan=3)
    button_forward = Button(root, text="forward >>", command=lambda: forward(img + 1))

    # img+1 as we want the next image to pop up
    if img == 8:
        button_forward = Button(root, text="Forward >>", state="disabled")

    # img-1 as we want previous image when we click back button
    button_back = Button(root, text="<< Back", command=lambda: back(img - 1))

    # Placing the button in new grid
    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=1)
    button_forward.grid(row=5, column=2)


def back(img):
    global label
    global button_forward
    global button_back
    global button_exit
    label.grid_forget()

    # for clearing the image for new image to pop up
    label = Label(image=List_images[img-1])
    label.grid(row=1, column=0, columnspan=3)

    button_back = Button(root, text="<< Back", command=lambda: back(img - 1))

    # whenever the first image will be there we will
    # have the back button disabled
    if img == 1:
        button_back = Button(root, state="disabled")

    label.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=1)
    button_forward.grid(row=5, column=2)


root = Tk()

root.title("Image_Viewer")
root.geometry("900x800")

img1 = ImageTk.PhotoImage(Image.open("image1.png"))
img2 = ImageTk.PhotoImage(Image.open("image2.png"))
img3 = ImageTk.PhotoImage(Image.open("image3.png"))
img4 = ImageTk.PhotoImage(Image.open("image4.png"))
img5 = ImageTk.PhotoImage(Image.open("image5.png"))
img6 = ImageTk.PhotoImage(Image.open("image6.png"))
img7 = ImageTk.PhotoImage(Image.open("image7.png"))
img8 = ImageTk.PhotoImage(Image.open("image1.jpeg"))

# List of the images so that we traverse the list
List_images = [img1, img2, img3, img4, img5, img6, img7, img8]

label = Label(image=img1)

# We have to show the box so this below line is needed
label.grid(row=1, column=0, columnspan=3)

# We have three button back ,forward and exit
button_back = Button(root, text="<< Back", command=back, state="disabled")
button_exit = Button(root, text="| Exit |", command=root.quit)
button_forward = Button(root, text="Forward >>", command=lambda: forward(1))

# placing the buttons in the frame
button_back.grid(row=5, column=0)
button_exit.grid(row=5, column=1)
button_forward.grid(row=5, column=2)

root.mainloop()

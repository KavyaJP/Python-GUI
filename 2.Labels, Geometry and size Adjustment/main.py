from tkinter import *

window = Tk()

window.title("TK")

# Adjust the window resolution
window.geometry("640x480")

# minsize and maxsize makes it so that your window can't be resized smaller or larger than these dimensions, dimensions are in pixels and width x height
window.minsize(480, 360)
window.maxsize(1280, 720)

# Create a label widget
label = Label(text="Hello World!")
label.pack()  # we need to pack the label to display it

window.mainloop()

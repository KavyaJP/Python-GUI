from tkinter import *

window = Tk()

window.title("Attributes of Labels and Packs")
window.geometry("640x480")

# important label options
# text - text to display
# image - image to display
# fg - foreground color
# bg - background color
# font - sets the Font
# padx - x padding
# pady - y padding
# relief - border style - SUNKEN, RAISED, GROOVE, RIDGE, FLAT, SOLID

label = Label(
    text="Hello World!",
    fg="white",
    bg="black",
    font=("Times New Roman", 36, "italic"),
    padx=40,
    pady=40,
    relief="solid",
)
label.pack()

# Important pack options
# anchor - nw, n, ne, w, center, e, sw, s, se
# side - top, bottom, left, right
# fill - x, y, both
# expand - True, False
# ipadx - internal x padding
# ipady - internal y padding

label2 = Label(text="Label", fg="White", bg="black", font=("arial", 24, "bold"))
label2.pack(side=BOTTOM, anchor="se", fill=BOTH, ipadx=20, ipady=20, expand=True)

window.mainloop()

from tkinter import *

window = Tk()
window.title("Images")
window.geometry("215x215")

# Create a label for displaying the image
photo = PhotoImage(file="C:\\Kavya\\Study\\Programs\\GUI\\3.Adding Images\\1.png")
label = Label(window, image=photo)
label.pack()

window.mainloop()

# There are some photos in a folder, read them using os library and display them using tkinter.
from tkinter import *
import os

window = Tk()
window.title("Photo Album")

# Get the current working directory
path = os.getcwd()
print(path)
# Get the list of files in the directory
files = os.listdir(path + "\\GUI\\Exercise\\Exercise1-PhotoAlbum\\photos")

# Display the photos
for file in files:
    if file.endswith(".png"):
        photo = PhotoImage(
            file=path + "\\GUI\\Exercise\\Exercise1-PhotoAlbum\\photos\\" + file
        )
        label_title = Label(text=file)
        label_title.pack()
        label_image = Label(image=photo)
        label_image.pack()

window.mainloop()

from tkinter import *
import PIL
from PIL import Image
from PIL import ImageTk

# to use PIL install first 
#sudo apt-get install python3-pil python3-pil.imagetk

root = Tk()

im = PIL.Image.open("photo.png")
photo = PIL.ImageTk.PhotoImage(im)

label = Label(root, image = photo)
label.image = photo  # keep a reference!
label.pack()

root.mainloop()
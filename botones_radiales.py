from tkinter import *

def seleccionar():
    monitor.config(text = "{}".format(option.get()))

def reset():
    option.set(None)
    monitor.config(text = "No seleccionado")

root = Tk()

option = IntVar()

Radiobutton(root, text = "opcion 1",variable = option, value = 1, command = seleccionar).pack()
Radiobutton(root, text = "opcion 2",variable = option, value = 2, command = seleccionar).pack()
Radiobutton(root, text = "opcion 3",variable = option, value = 3, command = seleccionar).pack()

monitor =Label(root)
monitor.pack()

Button(root, text = "reset", command = reset).pack()

root.mainloop()
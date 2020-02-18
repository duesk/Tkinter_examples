from tkinter import *

def seleccionar():
    cadena = ""
    if (leche.get()):
        cadena += "con leche "
    else:
        cadena += "sin leche "

    if (azucar.get()):
        cadena += "y con azucar"
    else:
        cadena += "y sin azucar"
    monitor.config(text = cadena)

root = Tk()

root.title("Cafeteria")
root.config(bd =15)

leche = IntVar()
azucar = IntVar()

imagen = PhotoImage(file = "imagen.gif")
Label(root, image = imagen).pack(side = "left")

frame = Frame(root)

Label(frame, text = "¿como quieres el cafe? ").pack(anchor = "w")
Checkbutton(frame, text = "con leche", variable = leche, onvalue = 1 , offvalue = 0, command = seleccionar ).pack(anchor = "w")
Checkbutton(frame, text = "con lazucar", variable = azucar, onvalue = 1 , offvalue = 0 , command = seleccionar).pack(anchor = "w")

frame.pack(side = "right")

monitor = Label(frame)
monitor.pack()

root.mainloop()
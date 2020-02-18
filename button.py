from tkinter import *


def hola():
    print("boton presionado")

def crear_label():
    Label(root, text = "label creada dinamicamente").pack()    

root = Tk()

#boton que imprime en consola
Button(root, text = "imprimir en consola", command = hola).pack()

#boton que crea una label cada que lo presionas 
Button(root, text = "Crear label ", command = crear_label).pack()

root.mainloop()
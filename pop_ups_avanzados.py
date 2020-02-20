from tkinter import *
from tkinter import colorchooser as colorchooser #para poder seleccionar color
from tkinter import filedialog as Filedialog

def test():
    color = colorchooser.askcolor( title = "elige un color", color = (255,0,25))
    print(color)

def open_file():
    ruta_archivo = Filedialog.askopenfilename(title = "selecciona un archivo", initialdir= "~/Escritorio",
                                                filetypes = (("gcode","*.gcode"), #dejar la coma en caso de ser solo un tipo de archivo filtrado
                                                            ("archivo de texto","*.txt")))
    print(ruta_archivo)

def save_file():            #equivale a open("ruta","w")
    ruta_save_file = Filedialog.asksaveasfile(title = "seleciona un archivo para guardar", initialdir = "~/Escritorio", mode = "w", defaultextension = ".txt")
    print(ruta_save_file)
    if ruta_save_file is not None:
        ruta_save_file.write("hola")
        ruta_save_file.close()

root = Tk()

Button(root, text = "seleccionar color ", command = test ).pack()
Button(root, text = "abrir  archivo", command = open_file).pack()
Button(root, text = "guardar archivo", command = save_file ).pack()

root.mainloop()
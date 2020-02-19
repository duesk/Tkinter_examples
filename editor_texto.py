from tkinter import *
from tkinter import filedialog as Filedialog
from io import open 
ruta = ""

def nuevo():
    global ruta
    mensaje.set("Nuevo")
    ruta = ""
    texto.delete(1.0,"end")
    root.title("Duesk text editor " + ruta)



def abrir():
    global ruta 
    mensaje.set("Abrir")
    ruta = Filedialog.askopenfilename(initialdir = "~/Escritorio", title = "Abrir archivo" , filetypes = (("archivos de texto", "*.txt"),)  )
    print(ruta)
    if ruta != "":
        archivo = open(ruta, "r")
        contenido = archivo.read()
        texto.delete(1.0,"end")
        texto.insert("insert", contenido)
        archivo.close()
        root.title("Duesk text editor " + ruta)


def guardar():
    global ruta 
    mensaje.set("Guardar")
    if ruta != "":
        contenido = texto.get(1.0,"end")
        archivo =  open(ruta, "w+")
        archivo.write(contenido)
        archivo.close()
        mensaje.set("Archivo guardado")

def guardar_como():
    global ruta 
    mensaje.set("Guardar como") 


root = Tk()
root.title("Duesk text editor")

menubar= Menu(root)
archivo_menu = Menu(menubar, tearoff = 0)
archivo_menu.add_command(label = "Nuevo", command = nuevo )
archivo_menu.add_command(label = "Abrir", command = abrir )
archivo_menu.add_command(label = "Guardar", command = guardar )
archivo_menu.add_command(label = "Guardar como", command = guardar_como)
archivo_menu.add_separator()
archivo_menu.add_command(label = "salir", command = root.quit)
menubar.add_cascade(menu = archivo_menu, label = "archivo")


texto = Text(root)
texto.pack(fill = "both", expand = 1)
texto.config(bd = 0, padx = 15, pady = 15, font  = ("Freemono", 15))

#  monitor inferior

mensaje = StringVar()
mensaje.set("Dusek tu editor esta activo")
monitor = Label(root, textvar = mensaje, justify = "left")
monitor.pack(side = "left")

root.config(menu = menubar)
root.mainloop()
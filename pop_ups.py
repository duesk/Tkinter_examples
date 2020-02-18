from tkinter import *
from tkinter import messagebox as Messagebox

root = Tk()
root.title("alertas")
root.minsize(250, 300)


def test():
    Messagebox.showinfo("titulo de la ventana de informacion", "contenido de la ventana")

def test2():
    Messagebox.showwarning("titulo de la alerta", "contenido de la ventana ")

def test3():
    Messagebox.showerror("titulo del error", "el error fallo exitosamente")

def salir():
    resultado = Messagebox.askquestion("titulo del la ventana ", "seguro que deseas salir")
    if (resultado == "yes"):
        root.destroy()

def ok_cancel():
    resultado = Messagebox.askokcancel("titulo del la ventana ", "seguro que deseas salir")
    if (resultado == True):
        root.destroy()

def yes_no():
    resultado = Messagebox.askyesno("titulo de la ventana","seguro que deseas salir")
    if resultado:
        root.destroy()

def yes_no_cancel():
    resultado = Messagebox.askyesnocancel("titulo de la ventana", "seguro que deseas salir")
    if resultado:
        root.destroy()

def retry_cancel():
    resultado = Messagebox.askretrycancel("titulo de  la ventana ","contenido de la ventana ")

Button(root, text = "info", command = test).pack()
Button(root, text = "Alerta", command = test2).pack()
Button(root, text = "error", command = test3).pack()
Button(root, text = "ok-Cancel", command = ok_cancel).pack()
Button(root, text = "Yes- No", command = yes_no).pack()
Button(root, text = "yes-no-cancel", command = yes_no_cancel).pack()
Button(root ,text= "retry - cancel", command = retry_cancel).pack()
Button(root, text = "salir", command = salir).pack()




root,mainloop()
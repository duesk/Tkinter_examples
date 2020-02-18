from tkinter import *

def sumar():
    r.set(float(n1.get()) + float(n2.get()))

def resta():
    r.set(float(n1.get()) - float(n2.get()))

def multi():
    r.set(float(n1.get()) * float(n2.get()))

def borrar():
    n1.set("")
    n2.set("")
    r.set("0.0")


root = Tk()
root.config(bd = 15)


n1 = StringVar()
n2 = StringVar()
r  = StringVar()
r.set("0.0")

Label(root, text = "numero uno").pack()
Entry(root,justify = "center", textvariable = n1).pack()



Label(root, text = "numero dos").pack()
Entry(root,justify = "center", textvariable = n2).pack()



Label(root, text = "numero resultado").pack()
Label(root,justify = "center", textvariable = r).pack()
Label(root, text = "").pack()



Button(root, text = "+", command = sumar).pack(side = "left")
Button(root, text = "-", command = resta).pack(side = "left")
Button(root, text = "X", command = multi).pack(side = "left")
Button(root, text = "borrar", command = borrar).pack(side = "left")




root.mainloop()

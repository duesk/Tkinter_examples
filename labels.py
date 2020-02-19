from tkinter import *

root = Tk()


#etiquetas
#   variable = Label(frame, text = "hola mundo")
#   label.place(x = 0, y = 0)

#crear label de forma sencilla 
#   Label(root, text = "equiqueta uno").pack()
#   Label(root, text = "equiqueta dos").pack()
#   Label(root, text = "equiqueta tres").pack()

#Label con posicionamiento.
#   Label(root, text = "equiqueta uno").pack(anchor = "nw")
#   Label(root, text = "equiqueta dos").pack(anchor = "center")
#   Label(root, text = "equiqueta tres").pack(anchor = "se")

#label como variable con modificaciones
#   label_modificada.config(bg = "green") # modificar el fondo de la etiqueta 
#   label_modificada.config(fg = "red")   #modificar el color de la fuente 
#   label_modificada.config(font = ("Garuda",25))
#   label_modificada = Label(root, text = "etiqueta modificada")
#   label_modificada.pack( anchor = "center")

imagen = PhotoImage(file = "imagen.gif")
Label(root, image = imagen, bd = 0).pack(side = "left")

variable_texto = StringVar()
variable_texto.set("hola")
Label(root, textvar = variable_texto).pack()

root.mainloop()
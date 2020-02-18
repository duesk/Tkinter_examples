from tkinter import *

root = Tk()

root.title("Cafeteria")
root.config(bd =15)

leche = IntVar()
azucar = IntVar()

Label(root, text = "como quieres el cafe? ").pack()
Checkbutton(root, text = "con leche", variable = leche, onvalue = 1 , offvalue = 0 ).pack()
Checkbutton(root, text = "con lazucar", variable = azucar, onvalue = 1 , offvalue = 0 ).pack()


root.mainloop()
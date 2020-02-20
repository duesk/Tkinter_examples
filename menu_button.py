from tkinter import *

def select():
    hola = Lb1.curselection()
    print(hola)



top = Tk()

Lb1 = Listbox(top)
Lb1.insert(6, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(1, "Ruby")

Lb1.pack()


Button(text = "select", command = select).pack()

top.mainloop()
from tkinter import *

root = Tk()

label = Label (root, text = "Texto muy largo")   #variable de una label
label.grid(row = 0, column = 0, sticky = "w")    #posicion en el grid

entry = Entry(root)                             
entry.grid(row = 0, column = 1)                  #poscicion en el grid

label2 = Label (root, text = "Texto")            #variable de una label
label2.grid(row = 1, column = 0, sticky = "w")   #poscicion en el grid

entry2 = Entry(root)                                
entry2.grid(row = 1, column = 1)                 #poscicion en el grid

root.mainloop()
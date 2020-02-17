from tkinter import *

root = Tk()

label = Label (root, text = "Texto muy largo")   #variable de una label
label.grid(row = 0, column = 0, sticky = "w", padx = 5, pady = 5)    #posicion en el grid

entry = Entry(root)                             
entry.grid(row = 0, column = 1, padx = 5, pady = 5)                  #poscicion en el grid      padx y pady son el pading
entry.config(justify = "right")                                      #inicias a escribir desde el centro 




label2 = Label (root, text = "Texto")                                #variable de una label
label2.grid(row = 1, column = 0, sticky = "w", padx = 5, pady = 5)   #poscicion en el grid

entry2 = Entry(root)                                
entry2.grid(row = 1, column = 1, padx = 5, pady = 5)                 #poscicion en el grid       padx y pady son el pading
entry2.config(justify = "center")                                     #inicias a escribir desde el centro 





label3 = Label (root, text = "otro texto")                                #variable de una label
label3.grid(row = 2, column = 0, sticky = "w", padx = 5, pady = 5)   #poscicion en el grid

entry3 = Entry(root)                                
entry3.grid(row = 2, column = 1, padx = 5, pady = 5)                 #poscicion en el grid       padx y pady son el pading
entry3.config(state = "disable")                                     #inicias a escribir desde el centro 




label4 = Label (root, text = "contraseña")                                #variable de una label
label4.grid(row = 3, column = 0, sticky = "w", padx = 5, pady = 5)   #poscicion en el grid

entry4 = Entry(root)                                
entry4.grid(row = 3, column = 1, padx = 5, pady = 5)                 #poscicion en el grid       padx y pady son el pading
entry4.config(show = "#")                                     #inicias a escribir desde el centro 


root.mainloop()
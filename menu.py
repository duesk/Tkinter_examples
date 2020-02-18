from tkinter import *

root = Tk()

menu_bar = Menu(root)
root.config(menu = menu_bar)

file_menu = Menu(menu_bar, tearoff = 0) # El tearoof evita que se cree una nueva ventana
file_menu.add_command(label = "nuevo")
file_menu.add_command(label = "nueva ventana ")
file_menu.add_separator()
file_menu.add_command(label = "guardar")
file_menu.add_command(label = "guardar como")



edit_menu = Menu(menu_bar, tearoff = 0)
edit_menu.add_command(label = "menu 1")
edit_menu.add_command(label = "menu 12")
edit_menu.add_command(label = "menu 123")
edit_menu.add_separator()
edit_menu.add_command(label = "menu 123")



selection_menu = Menu(menu_bar, tearoff = 0)
selection_menu.add_command(label = "menu a")
selection_menu.add_separator()
selection_menu.add_command(label = "menu ab")
selection_menu.add_command(label = "menu abc")
selection_menu.add_command(label = "menu abcd")



menu_bar.add_cascade(label = "archivo", menu = file_menu)
menu_bar.add_cascade(label = "archivo", menu = edit_menu)
menu_bar.add_cascade(label = "archivo", menu = selection_menu)

root.mainloop()
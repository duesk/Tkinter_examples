from tkinter import *

#para agregar colores rgb en tkinter
def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb  


root = Tk()

#title of window
root.title("title of window")

#min size of window
#   root.minsize(290, 700)

#resizable option 
#   root.resizable(1,1) you can lock the option to resizable window.
root.resizable(1,1) 

#window icon for Windows and mac
#   root.iconbitmap('icon.ico')

#fix the size of the frame
#   frame.config(with = 480, heigt = 320)
frame = Frame(root, width = 480, height = 320)
frame.pack() #Pack to Frame to renderize

#Change de cursor icon
#   frame.config(cursor= 'pirate')

#change background color
frame.config(bg = 'lightblue')

# Permite añadir borde a los widgets
#   frame.config(bd = 25)
#   frame.config(relief="sunken")   tipos de bordes disponibles flat, raised, sunken, groove, ridge.


#   frame.pack(side = "bottom", anchor ="se")   para fijar el frame 
#   frame.pack(fill = 'both', expand = 1)       permite rellanar en eje x o y de largo del contenedor
frame.pack()

#frame.config(bg=_from_rgb((240, 240, 240)))
frame.config(bg="lightblue")

#cambiar el color del fondo 
root.config(bg=_from_rgb((240, 240, 240)))

#Loop principal
root.mainloop()

#bottom of all code
root.mainloop()
from tkinter import *

root = Tk()

#title of window
root.title("title of window")

#min size of window
root.minsize(290, 700)


    #resizable option 
# root.resizable(1,1) you can lock the option to resizable window.
root.resizable(1,1) 


    #window icon for Windows and mac
#root.iconbitmap('icon.ico')

    # frame.config(with = 480, heigt = 320)  you can fix the size to frame 
frame = Frame(root, width = 480, height = 320)
frame.pack() #Pack to Frame to renderize

    #Change de cursor icon
#frame.config(cursor= 'pirate')

#change background color
frame.config(bg = 'lightblue')

frame.config(bd = 25)


#bottom of all code
root.mainloop()
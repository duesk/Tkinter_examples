# Python program to illustrate the concept 
# of threading 
# importing the threading module 
import threading 
from tkinter import *




  
def print_cube(): 
    """ 
    function to print cube of given num 
    """
    i = 0
    while True:
        i=i+1
        texto_label.set(str(i))
        text.pack()


if __name__ == "__main__": 
    root = Tk()
    # creating thread 
    texto_label = StringVar()
    texto_label.set("1")
    text = Label(root, textvar = texto_label )
    text.pack()
    
    t1 = threading.Thread(target=print_cube) 
  
    # starting thread 1 
    t1.start() 
 
    
    # both threads completely executed 

    root.mainloop()
 
from tkinter import *

#Instantiating window instance\
root = Tk() #this is a regular window
#Override settings of window
root.configure(bg="lime")
root.geometry('1440x720')
root.title("Minesweeper Project")
root.resizable(False, False)#It is all resizable, so we prevent it from that
#dividing windows into multiple frames


#Run the window
root.mainloop() #all code should be between this and root=Tk()
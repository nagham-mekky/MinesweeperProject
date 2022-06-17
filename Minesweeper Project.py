from tkinter import *
import settings

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb 
#Instantiating window instance\
root = Tk() #this is a regular window
#Override settings of window
root.configure(bg=rgb_hack((230, 230, 250))) #Add choose colour background
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Project")
root.resizable(False, False)#It is all resizable, so we prevent it from that
#dividing windows into multiple frames

top_frame = Frame( #Has title
    root,
    bg=rgb_hack((192, 192, 242)), #Change later
    width =1440, #same width of window
    height = 90
    ) 

top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg = rgb_hack((192, 192, 242)),
    width =180, 
    height = 630
)

left_frame.place(x=0, y=90)
#Run the window
root.mainloop() #all code should be between this and root=Tk()
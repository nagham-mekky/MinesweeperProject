from tkinter import *
import settings
import utils
def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb 
#Instantiating window instance\
root = Tk() #this is a regular window
#Override settings of window
root.configure(bg=rgb_hack((0, 0, 0))) #Add choose colour background
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Project")
root.resizable(False, False)#It is all resizable, so we prevent it from that
#dividing windows into multiple frames

top_frame = Frame( #Has title
    root,
    bg=rgb_hack((192, 192, 242)), #Change later
    width =settings.WIDTH, #same width of window
    height = utils.height_p(25)
    ) 

top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg = rgb_hack((192, 192, 242)),
    width =utils.width_p(25),  
    height = utils.height_p(75)
)

left_frame.place(x=0, y=utils.height_p(25))


center_frame = Frame(
    root,
    bg = rgb_hack((230, 230, 250)),
    width =utils.width_p(75),  
    height = utils.height_p(75)

)

center_frame.place(x=utils.width_p(25), y=utils.height_p(25))

# button1 = Button(
#     center_frame,
#     bg = 'light blue',
#     text = 'First Button'
# )
# button1.place(x=720,y=360)



#Run the window
root.mainloop() #all code should be between this and root=Tk()
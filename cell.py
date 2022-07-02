from tkinter import Button, Label
import settings
import utils
import random
from PIL import ImageTk, Image  
def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb 

class Cell:
    all = []
    cell_count_label_obj = None
    cell_count = settings.CELL_COUNT
    def __init__(self, x, y, mine=False):
        self.mine= mine
        self.cell_btn_obj = None
        self.x = x
        self.y = y

        #Apeedn obj to Cell.all list
        Cell.all.append(self)

    def create_btn_obj(self, location):
        btn = Button(
            location, 
            #text=f"{self.x},{self.y}",
            width = int(67.5/ settings.GRID_WIDTH),
            height = int(33.75 / settings.GRID_HEIGHT) #SEE IF U CAN MAKE MORE ACCUREATE
        )
       
        btn.bind('<Button-1>', self.left_click) #Left Click
        btn.bind('<Button-3>', self.right_click) #Right Click
        self.cell_btn_obj = btn
        #make image for flag
    
    @staticmethod
    def create_cell_count_label (location):
        lbl = Label (
            location,
            bg = rgb_hack((192, 192, 242)),
            #fg = 'white',
            text = f"Cells Left: {Cell.cell_count}",
            font = ("", 30)
        )
        Cell.cell_count_label_obj = lbl
        #return lbl

    def left_click (self, event):
        if (self.mine):
            self.show_mine()#end game, image of mine
        else:
            if self.mines_surrounded == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell() #check if a surrounding one is also 0
            self.show_cell()
        # print (event)
        # #print ("LEFT")
        # #print ("width ", (utils.width_p(75)))
        # print( "height " , int(33.75 / settings.GRID_HEIGHT))
    def show_mine(self):
        #Logic to interrupt game & display message that player lost
        self.cell_btn_obj.configure(bg='red') #(255,0,0)
        #Image of mine if mine clicked
    def get_cell_by_axis (self, x, y):
        #Return a cell obj based on (x,y)
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    @property            
    def surrounded_cells (self):
        cells = [self.get_cell_by_axis(self.x - 1, self.y -1 ),
        self.get_cell_by_axis(self.x - 1, self.y),
        self.get_cell_by_axis(self.x - 1, self.y + 1),
        self.get_cell_by_axis(self.x, self.y - 1),
        self.get_cell_by_axis(self.x + 1, self.y - 1),
        self.get_cell_by_axis(self.x + 1, self.y),
        self.get_cell_by_axis(self.x + 1, self.y + 1),
        self.get_cell_by_axis(self.x, self.y + 1)]
        
        cells = [cell for cell in cells if cell is not None]
        return(cells)

    @property
    def mines_surrounded (self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.mine:
                counter+=1
        return counter


    def show_cell(self):
        Cell.cell_count -=1
        self.cell_btn_obj.configure(text=self.mines_surrounded)
        #Replace the text of cell count label with new count
        if Cell.cell_count_label_obj:
            Cell.cell_count_label_obj.configure(
                text = f"Cells Left: {Cell.cell_count}"
            )

    def right_click (self, event):
        print (event)
        #print ("RIGHT")
        # Position text in frame
        ########FOR FLAG IMAGE
        # Label(root, text = 'Position image on button', font =('<font_name>', <font_size>)).pack(side = TOP, padx = <x_coordinate#>, pady = <y_coordinate#>)

        # # Create a photoimage object of the image in the path
        # photo = PhotoImage(file = "flag.png")

        # # Resize image to fit on button
        # photoimage = photo.subsample(1, 2)

        # # Position image on button
        # Button(root, image = photoimage,).pack(side = BOTTOM, pady = <y_coordinate#>)

    @staticmethod
    def randomize_mines():
        #my_list = ['Farahat', 'Joshua', 'Raith']
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT) #Change 9 to value that is determined depending on difficulty
        #print (picked_cells)
        for picked_cell in picked_cells:
            picked_cell.mine = True


    def __repr__(self):
        return f"Cell({self.x},{self.y})"
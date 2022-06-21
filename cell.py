from tkinter import Button
import settings
import utils
import random

class Cell:
    all = []
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
    
    def left_click (self, event):
        print (event)
        #print ("LEFT")
        #print ("width ", (utils.width_p(75)))
        print( "height " , int(33.75 / settings.GRID_HEIGHT))

    def right_click (self, event):
        print (event)
        #print ("RIGHT")

    @staticmethod
    def randomize_mines():
        #my_list = ['Farahat', 'Joshua', 'Raith']
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT) #Change 9 to value that is determined depending on difficulty
        #print (picked_cells)
        for picked_cell in picked_cells:
            picked_cell.mine = True


    def __repr__(self):
        return f"Cell({self.x},{self.y})"
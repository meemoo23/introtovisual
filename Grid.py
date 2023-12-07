#20 rows and 10 columns - top left cell will be 0,0 representing the origin. 
# To represent the gid a 2d array (lists of lists) will be used- empty cells are represented by 0, when a block is placed, 
# the cells will be assigned a value depending on its color (7 in total). The moving block is not reflected in the array. 

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30 
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)] #Creates a list of 0s in 20 rows and 10 columns
        self.colors = self.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()

    def get_cell_colors(self):

        dark_grey = (157, 157, 158) 
        green = (204, 255, 153)
        red = (255, 153, 153)
        orange = (255, 204, 153)
        yellow = (255, 255, 153)
        purple = (153, 153, 255)
        cyan = (153, 255, 255)
        blue = (153, 204, 255)

        return [dark_grey, green, red, orange, yellow, purple, cyan, blue] #the order is important as it will correspond to the ID of the block

    def draw(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column] #assigns the value of the cell to the variables and their values
                cell_rect = pygame.Rect(x, y, w, h) #esentially; x, y (coordinates), w (width), h (height) -- Rect is the cell (invisible)
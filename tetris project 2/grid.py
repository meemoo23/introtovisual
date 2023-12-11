#20 rows and 10 columns - top left cell will be 0,0 representing the origin. 
# To represent the gid a 2d array (lists of lists) will be used- empty cells are represented by 0, when a block is placed, 
# the cells will be assigned a value depending on its color (7 in total). The moving block is not reflected in the array. 

import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30 
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)] #Creates a list of 0s in 20 rows and 10 columns
        self.colors = Colors.get_cell_colors()
        
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()

    def is_inside(self, row, column): #Creates a boundary so the blocks cannot move outside of the grid space
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False

    
    def is_empty(self, row, column): #This checks if a cell block is empty (Blocks cannot fall ontop of one another)
        if self.grid[row][column] == 0:
            return True
        return False
    
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column] #assigns the value of the cell to the variables and their values
                cell_rect = pygame.Rect(column*self.cell_size +1, row*self.cell_size +1, self.cell_size -1, self.cell_size -1) #esentially; x, y (coordinates), w (width), h (height) -- Rect is the cell (invisible). The +1 is used to create a margin for the cell blocks.
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
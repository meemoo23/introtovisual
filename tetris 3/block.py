from colors import Colors
from position import Position
import pygame 


class Block: 
    def __init__(self, id): 
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0 #Used for moving the block up/down
        self.column_offset = 0 #Used for moving the block right/left
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns


    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles
    
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):  #Checks if the rotation state is equal to the number of rotation states (- the OBlock since it only has 1) and makes sure the rotation states can repeat
            self.rotation_state = 0

    def undo_rotation(self): #Checks that if the rotation occurs outside the grid, it cannot be rotated
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1 
       
    def draw(self, screen):
        tiles = self.get_cell_positions() #Retrieves the list of positions determined by the value of the rotation attribute
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size + 1, tile.row * self.cell_size + 1, self.cell_size -1, self.cell_size -1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect) #The color value is taken from the colors list using the block's own individual ID

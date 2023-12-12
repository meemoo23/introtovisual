#The Game Class holds all elements of the game such as the grid, current/next blocks and game state. 
from grid import Grid
from blocks import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0

    def update_score(self, lines_cleared, move_down_points): #Simplified Scoring System; 
        if lines_cleared == 1:
            self.score += 100 #100 points for a single line cleared
        elif lines_cleared == 2:
            self.score += 200 #200 points for a double line cleared
        elif lines_cleared == 3:
            self.score += 500 #500 points for a triple line cleared
        self.score 

    def get_random_block(self): #The next block that spawns will be randomised from the list
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks) #Each block should appear once in a cycle 
        self.blocks.remove(block) #Remove the block from the list if it has been used
        return block 
    
    def move_left(self):
        self.current_block.move(0, -1) #Moving the falling block to the left
        if self.block_inside() == False or self.block_fits() == False: #The block cannot move left across a block
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1) #Moving the falling block to the right
        if self.block_inside() == False or self.block_fits() == False:  #The block cannot move right across a block
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0) #Moving the falling block down
        if self.block_inside() == False or self.block_fits() == False: #If the cell is occupied, the move is undone and the block locks in place. 
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self): #Instead of moving left and right once reaching the bottom
        tiles = self.current_block.get_cell_positions() #The block locks in place by storing the ID of the block. 
        for position in tiles:
                self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block #Spawns the next block at the top of the screen
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        self.update_score(rows_cleared, 0)
        if self.block_fits() == False: #Game Over
            self.game_over = True

    def reset(self): #The grid has to be cleared in order to restart the game
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()] #Spawns the blocks again after reset
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0 #The score resets to 0 in a new game

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()  #If the cell is not occupied, it can move to that position (Stacking)
        for tile in tiles: 
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False: 
            self.current_block.undo_rotation()

    def block_inside(self): #Checks if any of the block is outside of the grid
        tiles = self.current_block.get_cell_positions()
        for tile in tiles: 
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)
        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 300, 300)
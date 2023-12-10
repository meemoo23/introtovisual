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

    def get_random_block(self): #The next block that spawns will be randomised from the list
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks) #Each block should appear once in a cycle 
        self.blocks.remove(block) #Remove the block from the list if it has been used
        return block 
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)
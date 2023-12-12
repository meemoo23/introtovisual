# How the blocks work: imagine a 3 x 3 grid, one for each one of the blocks 4 rotation states. 
# In the game, we only store the values needed for each rotation state (if that cell is occupied or not)
# To rotate a block, a state variable is used - if we update the occupied cells in the grid, the game will show which state.
# The inheritance method is used since all 7 blocks share similar properties of the parent class, the children class will make them unique. 
# If we want to move the block, all we have to do is move the origin point in the top left corner

from block import Block
from position import Position

# All blocks and their rotation shapes:
class LBlock(Block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [Position(0, 2), Position (1, 0), Position (1, 1), Position(1, 2)], #First rotation state - shows which cells are occupied/used
            1: [Position(0, 1), Position (1, 1), Position (2, 1), Position(2, 2)], #Second rotation state
            2: [Position(1, 0), Position (1, 1), Position (1, 2), Position(2, 0)], #Third rotation state
            3: [Position(0, 0), Position (0, 1), Position (1, 1), Position(2, 1)]  #Fourth rotation state
        }
        self.move(0, 3)

class JBlock(Block):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0: [Position(0, 0), Position (1, 0), Position (1, 1), Position(1, 2)], #First rotation state 
            1: [Position(0, 1), Position (0, 2), Position (1, 1), Position(2, 1)], #Second rotation state
            2: [Position(1, 0), Position (1, 1), Position (1, 2), Position(2, 2)], #Third rotation state
            3: [Position(0, 1), Position (1, 1), Position (2, 0), Position(2, 1)]  #Fourth rotation state
        }
        self.move(0, 3)

class IBlock(Block):
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0: [Position(1, 0), Position (1, 1), Position (1, 2), Position(1, 3)], #First rotation state 
            1: [Position(0, 2), Position (1, 2), Position (2, 2), Position(3, 2)], #Second rotation state
            2: [Position(2, 0), Position (2, 1), Position (2, 2), Position(2, 3)], #Third rotation state
            3: [Position(0, 1), Position (1, 1), Position (2, 1), Position(3, 1)]  #Fourth rotation state
        }
        self.move(-1, 3) #The Iblock has different starting position, one row must be removed

class OBlock(Block):
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            0: [Position(0, 0), Position (0, 1), Position (1, 0), Position(1, 1)], #First rotation state 
            1: [Position(0, 0), Position (0, 1), Position (1, 0), Position(1, 1)], #Second rotation state
            2: [Position(0, 0), Position (0, 1), Position (1, 0), Position(1, 1)], #Third rotation state
            3: [Position(0, 0), Position (0, 1), Position (1, 0), Position(1, 1)]  #Fourth rotation state
        }
        self.move(0, 4) #The OBlock has a different starting position to be centered

class SBlock(Block):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0: [Position(0, 1), Position (0, 2), Position (1, 0), Position(1, 1)], #First rotation state 
            1: [Position(0, 1), Position (1, 1), Position (1, 2), Position(2, 2)], #Second rotation state
            2: [Position(1, 1), Position (1, 2), Position (2, 0), Position(2, 1)], #Third rotation state
            3: [Position(0, 0), Position (1, 0), Position (1, 1), Position(2, 1)]  #Fourth rotation state
        }
        self.move(0, 3)

class TBlock(Block):
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0: [Position(0, 1), Position (1, 0), Position (1, 1), Position(1, 2)], #First rotation state 
            1: [Position(0, 1), Position (1, 1), Position (1, 2), Position(2, 1)], #Second rotation state
            2: [Position(1, 0), Position (1, 1), Position (1, 2), Position(2, 1)], #Third rotation state
            3: [Position(0, 1), Position (1, 0), Position (1, 1), Position(2, 1)]  #Fourth rotation state
        }
        self.move(0, 3)

class ZBlock(Block):
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
            0: [Position(0, 0), Position (0, 1), Position (1, 1), Position(1, 2)], #First rotation state 
            1: [Position(0, 2), Position (1, 1), Position (1, 2), Position(2, 1)], #Second rotation state
            2: [Position(1, 0), Position (1, 1), Position (2, 1), Position(2, 2)], #Third rotation state
            3: [Position(0, 1), Position (1, 0), Position (1, 1), Position(2, 0)]  #Fourth rotation state
        }
        self.move(0, 3)
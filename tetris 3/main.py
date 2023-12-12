import pygame, sys
from game import Game
from blocks import *

pygame.init()
dark_blue = (32, 42, 68) #Main Screen Color

screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("My Final Project")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT #A custom event in pygame that (in this game) creates an event for every time the block's position is updated
pygame.time.set_timer(GAME_UPDATE, 200) #The block should not have the same FPS, it needs to be slowed down to fall gradually (The block updates every 200 miliseconds)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        if event.type == pygame.KEYDOWN:
            if game.game_over == True: 
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False: #If the player presses the left arrow key, the block must move one cell to the left
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False: #Right key, moves to the right
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False: #Down key, moves down
                game.move_down()
            if event.key == pygame.K_UP and game.game_over == False: #Up key, rotates the blocks 
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False: #Game must stop ending if there is Game Over/ Press any key to reset the game
            game.move_down()

    screen.fill(dark_blue)
    game.draw(screen)
   
    pygame.display.update()
    clock.tick(60) #FPS rate
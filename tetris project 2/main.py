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
            if event.key == pygame.K_LEFT: #If the player presses the left arrow key, the block must move one cell to the left
                game.move_left()
            if event.key == pygame.K_RIGHT: #Right key, moves to the right
                game.move_right()
            if event.key == pygame.K_DOWN: #Down key, moves down
                game.move_down()
            if event.key == pygame.K_UP: #Up key, rotates the blocks 
                game.rotate()
        if event.type == GAME_UPDATE:
            game.move_down()

    screen.fill(dark_blue)
    game.draw(screen)
   
    pygame.display.update()
    clock.tick(60) #FPS rate
import pygame, sys
from Grid import Grid

pygame.init()
dark_blue = (32, 42, 68) #Main Screen Color

screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("My Final Project")

clock = pygame.time.Clock()

game_grid = Grid()
game_grid.print_grid()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

    screen.fill(dark_blue)
    pygame.display.update()
    clock.tick(60) #FPS rate
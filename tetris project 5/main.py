import pygame, sys
from game import Game
from colors import Colors
from blocks import *

pygame.init()

font_path = 'modern-tetris.ttf'
title_font = pygame.font.Font(font_path, 20) #Title font and size
score_surface = title_font.render("Your Score:", True, Colors.white)
next_surface = title_font.render("Next Block:", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

score_rect = pygame.Rect(340, 55, 210, 60) #Score Rectangle
next_rect = pygame.Rect(340, 215, 210, 180)

screen = pygame.display.set_mode((580,620))
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
                game.update_score(0, 1) #1 point is added everytime
            if event.key == pygame.K_UP and game.game_over == False: #Up key, rotates the blocks 
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False: #Game must stop ending if there is Game Over/ Press any key to reset the game
            game.move_down()

    score_value_surface = title_font.render(str(game.score), True, Colors.white) #Inside the game loop since it is not a static text and is dependent on the score

    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50)) #Block image transfer (A screen on a screen)
    screen.blit(next_surface, (365, 180, 50, 50))

    if game.game_over == True:
        screen.blit(game_over_surface, (365, 450, 50, 50)) #Game Over is only displayed if the game is actually over

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery)) #Since the score values get bigger, this function will guarantee that the score always stays in the middle
    pygame.draw.rect(screen, Colors.light_blue,next_rect, 0, 10)
    game.draw(screen)
   
    pygame.display.update()
    clock.tick(60) #FPS rate
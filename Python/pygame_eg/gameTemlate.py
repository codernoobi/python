#create a template for the game

import pygame
from pygame.locals import *

pygame.init()

#display surface
width=800
height=600
game_display = pygame.display.set_mode((width, height))

#title bar
pygame.display.set_caption('The Game')

#event handler for game loop
def eventHandler():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q)):
            pygame.quit()
            quit()

#game loop
while True:    
    eventHandler()
    pygame.display.update()
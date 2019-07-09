import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 700))

font = pygame.font.SysFont("comicsansms", 72)
text = font.render("Hello, World", True, (0, 128, 0))

#get all fonts
# all_fonts = pygame.font.get_fonts()
# def make_font(all_fonts, size):
#     available = pygame.font.get_fonts()
#     # get_fonts() returns a list of lowercase spaceless font names 
#     choices = map(lambda x:x.lower().replace(' ', ''), fonts)
#     for choice in choices:
#         if choice in available:
#             return pygame.font.SysFont(choice, size)
#     return pygame.font.Font(None, size)

def eventHandler():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q)):
            pygame.quit()
            quit()

        if event.type == KEYDOWN and event.key == K_t:
            screen.fill((255, 255, 255))
            screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))

while True:
    eventHandler()
    pygame.display.update()

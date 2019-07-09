import pygame
from pygame.locals import *

pygame.init()

w=800
h=700
screen=pygame.display.set_mode((w,h))

def eventHandler():
    left=50
    top=50
    width=70
    height=70
    color=(0,255,0)
    radius=100
    point_list=[(250,250),(350,250),(400,400),(350,450),(250,450),(200,400)]            
    
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q)):
            pygame.quit()
            quit()

        if event.type == KEYDOWN and event.key == K_r:
            screen.fill((0, 0, 0))
            color=(255,0,0)
            pygame.draw.rect(screen, color, pygame.Rect(50, 50, 70, 70))
            pygame.draw.rect(screen, color, pygame.Rect(250, 250, 70, 70),10)

        if event.type == KEYDOWN and event.key == K_c:
            screen.fill((0, 0, 0))
            pygame.draw.circle(screen, color, (200, 200), radius)
            pygame.draw.circle(screen, color, (400, 400), radius,10)

        if event.type == KEYDOWN and event.key == K_p:
            screen.fill((0, 0, 0))
            pygame.draw.polygon(screen, color, point_list)

        if event.type == KEYDOWN and event.key == K_l:
            screen.fill((0, 0, 0))
            pygame.draw.line(screen, color, (50,50),(150,150),10)  #(startX, startY), (endX, endY), width)


while True:    
    eventHandler()
    pygame.display.update()
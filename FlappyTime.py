import pygame
from pygame.locals import *

pygame.init()

window_width = 864
window_height = 936

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Flappy Time")


#load images
background = pygame.image.load('img/background.png')


run = True
while run:

    window.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    

pygame.quit()

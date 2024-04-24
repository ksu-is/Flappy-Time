import pygame
from pygame.locals import *

pygame.init()

#frames per sec (for the scroll to move smoother)
clock = pygame.time.Clock()
fps = 60

window_width = 864
window_height = 936

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Flappy Time")


#define game variables
ground_scroll = 0
scroll_speed = 4


#load images
bg = pygame.image.load('bg.png')
ground_img = pygame.image.load('ground.png')

#add finn character and prepare to animate
class Finn(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)


run = True
while run:

    #call fps
    clock.tick(fps)
    
    #draw background
    window.blit(bg, (0,0))
    
    #draw and scroll the gorund
    window.blit(ground_img, (ground_scroll,768))
    ground_scroll -= scroll_speed
    
    #continues scroll effect
    if abs(ground_scroll) > 35:
        ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    

pygame.quit()

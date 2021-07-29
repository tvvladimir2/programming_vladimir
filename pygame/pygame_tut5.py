# Tutorial at:
# https://www.youtube.com/watch?v=iLL2V1es52I&list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq&index=3

import pygame # import pygame
import sys

pygame.init() # initialize pygame

# Define colors
white = (255,255,255)
black = (0,0,0)
red=(255,0,0)

# Surface
gameDisplay = pygame.display.set_mode((800,600)) # set up a screen / display # Tuple collection variable
pygame.display.set_caption('Slither')


gameExit = False # specify a constant variable

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        print (event) #print every event handling happening

    gameDisplay.fill(red) # RGB fill color
    pygame.display.update()

pygame.quit() # uninitialize pygame
quit()

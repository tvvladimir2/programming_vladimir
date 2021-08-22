# Tutorial at:
# https://www.youtube.com/watch?v=iLL2V1es52I&list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq&index=3

import pygame # import pygame
import sys

pygame.init() # initialize pygame

# Surface
gameDisplay = pygame.display.set_mode((800,600)) # set up a screen / display # Tuple collection variable
pygame.display.set_caption('Slither')

pygame.display.update()
gameExit = False # specify a constant variable

# main game loop
while not gameExit:
    for event in pygame.event.get():
        print (event) #print every event handling happening
    # gameExit = True

pygame.quit() # uninitialize pygame
quit()

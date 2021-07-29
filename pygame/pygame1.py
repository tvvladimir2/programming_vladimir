# Tutorial at:
# https://www.youtube.com/watch?v=sVbFS9qEl4Y&list=PL2mJQcs6jRvhQXvLNVyZ1Q7r7Uf1d4AlX&index=2

import pygame # import pygame
import sys

pygame.init() # initialize pygame

# Surface
gameDisplay = pygame.display.set_mode((800,600)) # set up a screen / display # Tuple collection variable
clock = pygame.time.Clock()

# class Player: # Didn't study classes yet, stopped the tutorial at 3m:47s

while True:
    display.fill((0,0,0)) # RGB fill color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() # import sys # quit from python script
            pygame.QUIT # quit from pygame

    clock.tick(60) # Run the game 60 Frames per second
    pygame.display.update()

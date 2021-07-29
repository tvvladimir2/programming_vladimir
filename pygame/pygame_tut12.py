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

# Variables
gameExit = False # specify a constant variable

lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock() # initiate a sleep function that forces our game to be exactly frames per second

# Loop
while not gameExit:
    # event loop
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameExit = True

        print (event) #print every event handling happening

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -2
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = +2
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -2
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = +2
                lead_x_change = 0
        #
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                lead_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                lead_y_change = 0

    # Define boundaries
    if lead_x >= 800 or lead_x <=0 or lead_y >=600 or lead_y <=0:
        gameExit = True

    # logic loop
    lead_x += lead_x_change
    lead_y += lead_y_change

    gameDisplay.fill(red) # RGB fill color
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10,10])
    pygame.display.update()

    clock.tick(60) # Define frames per second #

pygame.quit() # uninitialize pygame
quit()

# Tutorial at:
# https://www.youtube.com/watch?v=iLL2V1es52I&list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq&index=3

import pygame # import pygame
import sys

pygame.init() # initialize pygame

# Define colors
white = (255,255,255)
black = (0,0,0)
red=(255,0,0)
salat=(50,231,231)
green=(52,218,68)
greendark=(179,235,35)

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
            if event.key == pygame.K_a:
                lead_x_change = -2
            if event.key == pygame.K_d:
                lead_x_change = +2
            if event.key == pygame.K_w:
                lead_y_change = -2
            if event.key == pygame.K_s:
                lead_y_change = +2

    # logic loop
    lead_x += lead_x_change
    lead_y += lead_y_change

    gameDisplay.fill(green) # RGB fill color
    pygame.draw.rect(gameDisplay, salat, [lead_x, lead_y, 10,10])
    pygame.display.update()

    clock.tick(30) # Define frames per second #

pygame.quit() # uninitialize pygame
quit()

# Tutorial at:
# https://www.youtube.com/watch?v=iLL2V1es52I&list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq&index=3
# Fixing the hardcoding, adding variables

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
# Display Variables
display_width = 800
display_height = 600

# Variables
gameExit = False # specify a constant variable

lead_x = display_width / 2
lead_y = display_height / 2
lead_x_change = 0
lead_y_change = 0

block_size = 10

clock = pygame.time.Clock() # initiate a sleep function that forces our game to be exactly frames per second

frameRate = 60

# Surface
gameDisplay = pygame.display.set_mode((display_width, display_height)) # set up a screen / display # Tuple collection variable
pygame.display.set_caption('Slither')

# Loop
while not gameExit:
    # event loop
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameExit = True

        print (event) #print every event handling happening

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                lead_x_change = -block_size
                lead_y_change = 0
            elif event.key == pygame.K_d:
                lead_x_change = +block_size
                lead_y_change = 0
            elif event.key == pygame.K_w:
                lead_y_change = -block_size
                lead_x_changed = 0
            elif event.key == pygame.K_s:
                lead_y_change = +block_size
                lead_x_change = 0
            elif event.key == pygame.K_SPACE: #Stops the movement
                lead_x_change = 0
                lead_y_change = 0
            #diagonal experimental movement
            elif event.key == pygame.K_q:
                lead_x_change = -2
                lead_y_change = -2
            elif event.key == pygame.K_e:
                lead_x_change = +2
                lead_y_change = -2
            elif event.key == pygame.K_z:
                lead_x_change = -2
                lead_y_change = +2
            elif event.key == pygame.K_c:
                lead_x_change = +2
                lead_y_change = +2
            elif event.key == pygame.K_r:
                lead_x = display_width / 2
                lead_y = display_height / 2
                lead_x_change =-0
                lead_y_change =-0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                lead_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                lead_y_change = 0

    # Define boundaries
    if lead_x >= display_width or lead_x <=0 or lead_y >=display_height or lead_y <=0:
        gameExit = True

    # logic loop
    lead_x += lead_x_change
    lead_y += lead_y_change

    gameDisplay.fill(green) # RGB fill color
    pygame.draw.rect(gameDisplay, red, [lead_x, lead_y, block_size, block_size])
    pygame.display.update()

    clock.tick(frameRate) # Define frames per second #

pygame.quit() # uninitialize pygame
quit()

# Tutorial at:
# https://www.youtube.com/watch?v=iLL2V1es52I&list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq&index=3

import pygame # import pygame
import sys
import time

pygame.init() # initialize pygame

# Define colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

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

font = pygame.font.SysFont(name = None, size = int(display_height/4))

# Surface
gameDisplay = pygame.display.set_mode((display_width, display_height)) # set up a screen / display # Tuple collection variable
pygame.display.set_caption('Slither')

def message_to_screen (message, color):
    screen_text = font.render(message, True, color)
    gameDisplay.blit(source = screen_text, dest = [display_width/2, display_height/2])

# Loop
while not gameExit:
    # event loop
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameExit = True

        print (event) #print every event handling happening

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -block_size
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = +block_size
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -block_size
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = +block_size
                lead_x_change = 0
        #
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

    gameDisplay.fill(red) # RGB fill color
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, block_size, block_size])
    pygame.display.update()

    clock.tick(frameRate) # Define frames per second #

message_to_screen("You lose", white)
pygame.display.update() # must update the screen in order to show the final message
time.sleep(5)
pygame.quit() # uninitialize pygame
quit()

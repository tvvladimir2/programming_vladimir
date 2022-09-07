# Tutorial at:
# https://www.youtube.com/watch?v=iLL2V1es52I&list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq&index=3

import pygame # import pygame
import sys
import math

pygame.init() # initialize pygame

# Define colors
white = (255,255,255)
black = (0,0,0)
red=(255,0,0)
salat=(50,231,231)
green=(52,218,68)
greendark=(179,235,35)

# Surface
gameDisplay = pygame.display.set_mode((1000,1000)) # set up a screen / display # Tuple collection variable
pygame.display.set_caption('Slither')
#character animation
from pygame_functions import *

testSprite = makeSprite("images/links.gif", 32)
moveSprite(testSprite,300,300,True)
showSprite(testSprite)

nextFrame = clock()

frame = 0

while True:
    if clock() > nextFrame:
        frame = (frame+1)%8
        nextFrame += 80
    if keypressed("right"):
        changeSpriteImage(testSprite, 0*8 + frame)

    elif keypressed("down"):
        changeSpriteImage(testSprite, 1*8 + frame)

    elif keypressed("left"):
        changeSpriteImage(testSprite, 2*8 + frame)

    elif keypressed("up"):
        changeSpriteImage(testSprite, 3*8 + frame)

    else:
        changeSpriteImage(testSprite, 1 * 8 + 5)

    tick(120)

endWait()
# Variables
gameExit = False # specify a constant variable
# gameWin = False # win condition

#player1
lead_x = 200
lead_y = 300
lead_x_change = 0
lead_y_change = 0
#player2
lead_x2 = 600
lead_y2 = 300
lead_x2_change = 0
lead_y2_change = 0

clock = pygame.time.Clock() # initiate a sleep function that forces our game to be exactly frames per second

# Loop
while not gameExit:
    # event loop
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameExit = True

        print (event) #print every event handling happening
                   # PLAYER 1
        if event.type == pygame.KEYDOWN:
            #player1
            if event.key == pygame.K_a:
                lead_x_change = -2
            if event.key == pygame.K_d:
                lead_x_change = +2
            if event.key == pygame.K_w:
                lead_y_change = -2
            if event.key == pygame.K_s:
                lead_y_change = +2
            #player2
            if event.key == pygame.K_LEFT:
                lead_x2_change = -2
            if event.key == pygame.K_RIGHT:
                lead_x2_change = +2
            if event.key == pygame.K_UP:
                lead_y2_change = -2
            if event.key == pygame.K_DOWN:
                lead_y2_change = +2

        if event.type == pygame.KEYUP:
            #player 1
            if event.key == pygame.K_d or event.key == pygame.K_a:
                lead_x_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                lead_y_change = 0
            #player 2
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                lead_x2_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                lead_y2_change = 0

    # logic loop
    #player1
    lead_x += lead_x_change
    lead_y += lead_y_change
    #player1
    lead_x2 += lead_x2_change
    lead_y2 += lead_y2_change

    gameDisplay.fill(green) # RGB fill color
    pygame.draw.rect(gameDisplay, salat, [lead_x, lead_y, 10,10]) #spawn player1
    pygame.draw.rect(gameDisplay, red, [lead_x2, lead_y2, 10,10]) #spawn player2
    pygame.draw.line(Surface, color, start_pos, end_pos, width) # draw a line between them
    pygame.display.update()

    # ab = math.sqrt((lead_x-lead_x2)**2 + (lead_y-lead_y2)**2)
    # if ab <= 10:
    if abs(lead_x-lead_x2)<10 and abs(lead_y-lead_y2)<10:
        gameExit = True


    clock.tick(60) # Define frames per second #

pygame.quit() # uninitialize pygame
quit()

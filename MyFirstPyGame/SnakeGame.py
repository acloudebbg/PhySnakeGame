# Snake Game !
import pygame
import sys
import random
import time

check_errors = pygame.init()

if check_errors[1] != 0:
    print (" (!) Had {0} Initializing errors, exiting ...".format(check_errors[1]))
    sys.exit(-1)
else:
    print ("(+) PyGame successfully initialized!")

#Play surface
playsurface = pygame.display.set_mode((720,460))
pygame.display.set_caption("Snake game !")

#Colors
red = pygame.Color(255,0,0) #Game over
green = pygame.Color(0,255,0) #Snake
blue = pygame.Color(0,0,255)  # To use at your discretion
black = pygame.Color(0,0,0) #score
white = pygame.Color(255,255,255) # background
brown = pygame.Color(165,42,42)  #food

# FPS controller
fpsController = pygame.time.Clock()

#Important variables
#initial snake coordinates
snakePos = [100,50]
snakeBody = [[100,50][90,50][80,50]]




time.sleep(5)
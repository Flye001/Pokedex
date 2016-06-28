import pygame, sys
from pygame.locals import *
import time

psyduckk = '/home/pi/pokedex/psyduck.png'

pygame.init()
screen = pygame.display.set_mode((475,475),0,32)
psyduck = pygame.image.load(psyduckk).convert_alpha()

screen.blit(psyduck, (0,0))
pygame.display.update()
time.sleep(5)
pygame.quit()
sys.exit()

import pygame, sys
from pygame.locals import *
import time

black = (0,0,0)
#self.screen = pygame.display.set_mode((600,400), 0, 32)

pygame.init()
screen = pygame.display.set_mode((475,475),0,32)
poke_ball = 'pokeball.png'
pokemon_ball = pygame.image.load(poke_ball).convert_alpha()
screen.blit(pokemon_ball, (0,0))
pygame.display.update()

pokemon2 = raw_input('Enter a Pokemon name: ')
str(pokemon2)
pokemon1 = pokemon2 + '.png'
print(pokemon1)

pokemon = pygame.image.load(pokemon1).convert_alpha()

while True:
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
	screen.fill(black)
        screen.blit(pokemon, (0,0))
        pygame.display.update()

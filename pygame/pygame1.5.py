import pygame, sys
from pygame.locals import *

pygame.init()
pokemon2 = raw_input('Enter a Pokemon name: ')
str(pokemon2)
pokemon1 = pokemon2 + '.png'
print(pokemon1)
screen = pygame.display.set_mode((475,475),0,32)
pokemon = pygame.image.load(pokemon1).convert_alpha()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	status = pygame.key.get_focused()
	if status == True:
		pygame.quit()
		sys.exit()
	screen.blit(pokemon, (0,0))
	pygame.display.update()

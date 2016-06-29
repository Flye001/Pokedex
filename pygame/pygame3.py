import pygame, sys
from pygame.locals import *
import time
import os

def start():
	os.system('clear')
	black = (0,0,0)
	pygame.init()
	screen = pygame.display.set_mode((475,475),0,32)
	screen.fill(black)
	poke_ball = 'pokeball.png'
	pokemon_ball = pygame.image.load(poke_ball).convert_alpha()
	screen.blit(pokemon_ball, (0,0))
	pygame.display.update()
	pokemon2 = raw_input('Enter a Pokemon name: ')
	str(pokemon2)
	pokemon1 = pokemon2 + '.png'
	os.system('clear')
	print('Press Backspace to go back')
	pokemon = pygame.image.load(pokemon1).convert_alpha()
	
	while True:
        	for event in pygame.event.get():
                	if event.type == QUIT:
                        	pygame.quit()
                        	sys.exit()
		#pygame.event.set_grab()
		key = pygame.key.get_focused()
		#print(key)
		if key == True:
			start()
		screen.fill(black)
        	screen.blit(pokemon, (0,0))
        	pygame.display.update()

start()

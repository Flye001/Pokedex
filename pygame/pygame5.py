import pygame, sys
from pygame.locals import *
import time
import os
from gpiozero import LED
from gpiozero import Button

red = LED(17)
orange = LED(18)
green = LED(19)
button1 = Button(2)
button2 = Button(3)

def start():
	os.system('clear')
	red.on()
	orange.off()
	green.off()
	black = (0,0,0)
	pygame.init()
	screen = pygame.display.set_mode((475,475),0,32)
	screen.fill(black)
	poke_ball = 'pokeball.png'
	pokemon_ball = pygame.image.load(poke_ball).convert_alpha()
	screen.blit(pokemon_ball, (0,0))
	pygame.display.update()
	while True:
		if button1.is_pressed:
			red.off()
			orange.on()
			green.off()
			pokemon2 = raw_input('Enter a Pokemon name: ')
			str(pokemon2)
			pokemon1 = pokemon2 + '.png'
			os.system('clear')
			print('Press the reset to go back')
			pokemon = pygame.image.load(pokemon1).convert_alpha()
			break
		
	while True:
		red.off()
		orange.off()
		green.on()
        	for event in pygame.event.get():
                	if event.type == QUIT:
                        	pygame.quit()
                        	sys.exit()
		#pygame.event.set_grab()
		#key = pygame.key.get_focused()
		#print(key)
		#if key == True:
		#	start()
		if button2.is_pressed:
			start()
		screen.fill(black)
        	screen.blit(pokemon, (0,0))
        	pygame.display.update()

start()

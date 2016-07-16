import pygame, sys
from pygame.locals import *
import time
import os
from gpiozero import LED
from gpiozero import Button
from matrix_keypad import RPi_GPIO

#red = LED(17)
#orange = LED(18)
#green = LED(19)
#blue = LED(10)
button1 = Button(2)
button2 = Button(3)

kp = RPi_GPIO.keypad(columnCount = 4)

def digit():
	r = None
	while r == None:
		r = kp.getKey()
	return r

def start():
	os.system('clear')
	print('Loading...')
	#red.on()
	#orange.off()
	#green.off()
	#blue.off()
	black = (0,0,0)
	pygame.init()
	screen = pygame.display.set_mode((475,475),0,32)
	screen.fill(black)
	poke_ball = '/home/pi/pokedex/pokes/pokeball.png'
	pokemon_ball = pygame.image.load(poke_ball).convert_alpha()
	screen.blit(pokemon_ball, (0,0))
	pygame.display.update()
	os.system('clear')
	print('Press the scan (blue) button to scan')
	print('Press the reset (red) button to exit')
	while True:
		if button1.is_pressed:
			os.system('clear')
			#red.off()
			#orange.on()
			#blue.on()
			#green.off()
			screen.fill(black)
			bars1 = '/home/pi/pokedex/pokes/bars.png'
			bars = pygame.image.load(bars1).convert_alpha()
			screen.blit(bars, (0,0))
			pygame.display.update()
			print('Enter a Pokemon number: ')
			pp1 = digit()
			#print pp1
			time.sleep(1)
			pp2 = digit()
                        #print pp2
                        time.sleep(1)
			pp3 = digit()
                        #print pp3
                        p1 = str(pp1)
			p2 = str(pp2)
			p3 = str(pp3)
			pokemon2 = p1+p2+p3
			#print(pokemon2)
			pokemon1 = '/home/pi/pokedex/pokes/' + pokemon2 + '.png'
			os.system('clear')
			print('Press the reset (red) button to go back')
			pokemon = pygame.image.load(pokemon1).convert_alpha()
			break
		if button2.is_pressed:
			os.system('clear')
			pygame.quit()
			sys.exit()

	while True:
		#red.off()
		#orange.off()
		#blue.off()
		#green.on()
		if button2.is_pressed:
			start()
		screen.fill(black)
        	screen.blit(pokemon, (0,0))
        	pygame.display.update()

start()

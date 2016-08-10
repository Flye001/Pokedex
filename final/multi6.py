import pygame
import sys
import time
import os
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI
from gpiozero import LED
from gpiozero import Button
from pygame.locals import *
from matrix_keypad import RPi_GPIO
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image

DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

red = LED(4)
orange = LED(5)
green = LED(6)
blue = LED(7)
button1 = Button(2)
button2 = Button(3)
wait = 0.5

kp = RPi_GPIO.keypad(columnCount = 4)
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

disp.begin(contrast=30)

def digit():
	r = None
	while r == None:
		r = kp.getKey()
	return r

def clearLCD():
	#image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
	#draw = ImageDraw.Draw(image)
	#draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=0, fill=255)
	#disp.image(image)
	#disp.display()
	disp.clear()
	disp.display()

def printLCD(LCDtext,LCDx,LCDy):
	#start()
	image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
	# Gedisp.image(image)
	disp.display()
	#t drawing object to draw on image.
	draw = ImageDraw.Draw(image)
	# Draw a white filled box to clear the image.
	draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
	# Load default font.
	font = ImageFont.load_default()
	# Alternatively load a TTF font.
	# Some nice fonts to try: http://www.dafont.com/bitmap.php
	# font = ImageFont.truetype('Minecraftia.ttf', 8)
	# Write some text.
	draw.text((LCDx,LCDy), LCDtext, font=font)
	# Display image.
	disp.image(image)
	disp.display()

def imageLCD(LCDimage):
	clearLCD()
	LCDpoke = str(LCDimage)
	Opoke = '/home/pi/pokedex/pokes/' + LCDpoke + '.png'
	poke = str(Opoke)
	image = Image.open(poke).resize((LCD.LCDWIDTH, LCD.LCDHEIGHT), Image.ANTIALIAS).convert('1')
	disp.image(image)
	disp.display()

def start():
	clearLCD()
	printLCD('Loading...', 0, 0)
	os.system('clear')
	print('Loading...')
	red.on()
	orange.off()
	green.off()
	blue.off()
	black = (0,0,0)
	pygame.init()
	screen = pygame.display.set_mode((475,475),0,32)
	screen.fill(black)
	poke_ball = '/home/pi/pokedex/pokes/pokeball.png'
	pokemon_ball = pygame.image.load(poke_ball).convert_alpha()
	screen.blit(pokemon_ball, (0,0))
	time.sleep(3)
	pygame.display.update()
	imageLCD('pokeball')
	os.system('clear')
	print('Press the scan (blue) button to scan')
	print('Press the reset (red) button to exit')
	while True:
		if button1.is_pressed:
			os.system('clear')
			red.off()
			orange.on()
			blue.on()
			green.off()
			screen.fill(black)
			bars1 = '/home/pi/pokedex/pokes/bars.png'
			bars = pygame.image.load(bars1).convert_alpha()
			screen.blit(bars, (0,0))
			pygame.display.update()
			clearLCD()
			printLCD('Enter a number:', 0, 0)
			print('Enter a Pokemon number: ')
			pp1 = digit()
			pdisplay = str(pp1)
			printLCD(pdisplay, 0, 0)
			print pp1
			time.sleep(wait)
			pp2 = digit()
			ppdisplay = str(pp2)
			pdisplay1 = pdisplay + ppdisplay
			printLCD(pdisplay1, 0, 0)
                        print pp2
                        time.sleep(wait)
			pp3 = digit()
			ppdisplay = str(pp3)
			pdisplay = pdisplay1 + ppdisplay
			printLCD(pdisplay,  0, 0)
                        print pp3
                        p1 = str(pp1)
			p2 = str(pp2)
			p3 = str(pp3)
			pokemon2 = p1+p2+p3
			check = int(pokemon2)
			if check >=152:
				blue.off()
				green.off()
				orange.off()
				red.off()
				pokeerror = 0
				while pokeerror == 0:
					clearLCD()
					printLCD('ERROR!!!', 0, 0)
					os.system('clear')
					print ("THAT'S NOT A POKEMON!!!")
					print('Press the reset (red) button to go back')
					pokemon1 = '/home/pi/pokedex/pokes/pokeball.png'
					pokemon = pygame.image.load(pokemon1).convert_alpha()
					if button2.is_pressed:
						start()
					red.on()
					time.sleep(0.25)
					red.off()
			pokemon1 = '/home/pi/pokedex/pokes/' + pokemon2 + '.png'
			imageLCD(pokemon2)
			os.system('clear')
			print 'Now Showing Pokemon: ', pokemon2
			print('Press the reset (red) button to go back')
			pokemon = pygame.image.load(pokemon1).convert_alpha()
			break
		if button2.is_pressed:
			os.system('clear')
			clearLCD()
			pygame.quit()
			sys.exit()

	while True:
		red.off()
		orange.off()
		blue.off()
		green.on()
		if button2.is_pressed:
			start()
		screen.fill(black)
        	screen.blit(pokemon, (0,0))
        	pygame.display.update()

clearLCD()
start()

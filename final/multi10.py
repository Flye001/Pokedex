import pygame
import sys
import time
import os
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI
from picamera import PiCamera
from gpiozero import LED
from gpiozero import Button
from pygame.locals import *
from matrix_keypad import RPi_GPIO
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

camera = PiCamera()

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
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
disp.begin(contrast=50)
pygame.init()
screen = pygame.display.set_mode((475,475),0,32)
black = (0,0,0)

def cameratest():
	camera.resolution = (475, 475)
	camera.start_preview()
	while True:
		if button1.is_pressed:
			camera.capture('/home/pi/pokedex/CameraOut/pokemon.png')
			camera.stop_preview()
			imbg = Image.open("/home/pi/pokedex/CameraOut/pokemon.png")
			imfg = Image.open("/home/pi/pokedex/images/025.png")
			imfg = imfg.resize((118, 118))
			new_im = Image.new('RGBA', (475,475))
			new_im.paste(imfg,(0,0))
			## Add any logos here with new_im.paste(imfg,(??,??))
			imbg.paste(new_im, None, new_im)
			imbg.save("/home/pi/pokedex/CameraOut/overlay.png", "png")
        		screen.fill(black)
        		poke_ball = '/home/pi/pokedex/CameraOut/overlay.png'
        		pokemon_ball = pygame.image.load(poke_ball).convert_alpha()
	        	screen.blit(pokemon_ball, (0,0))
			pygame.display.update()
			time.sleep(10)
			start()
			break

def digit():
	r = None
	while r == None:
		r = kp.getKey()
	return r

def clearLCD():
	disp.clear()
	draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
	disp.image(image)
	disp.display()
	disp.display()

def printLCD(LCDtext,LCDx,LCDy):
	draw.text((LCDx,LCDy), LCDtext, font=font)
	disp.image(image)

def updateLCD():
	disp.display()

def imageLCD(LCDimage):
	clearLCD()
	LCDpoke = str(LCDimage)
	Opoke = '/home/pi/pokedex/images/' + LCDpoke + '.png'
	poke = str(Opoke)
	image = Image.open(poke).resize((LCD.LCDWIDTH, LCD.LCDHEIGHT), Image.ANTIALIAS).convert('1')
	disp.image(image)
	disp.display()

def start():
	clearLCD()
	printLCD('Loading...', 0, 0)
	updateLCD()
	os.system('clear')
	print('Loading...')
	red.on()
	orange.off()
	green.off()
	blue.off()
	screen.fill(black)
	poke_ball = '/home/pi/pokedex/images/Logo.png'
	pokemon_ball = pygame.image.load(poke_ball).convert_alpha()
	screen.blit(pokemon_ball, (0,0))
	time.sleep(1)
	pygame.display.update()
	clearLCD()
	printLCD('Press the', 0, 0)
	printLCD('blue button', 0, 10)
	printLCD('to start.', 0, 20)
	updateLCD()
	os.system('clear')
	print('Press the scan (blue) button to scan')
	print('Press the reset (red) button to exit')
	while True:
		if button1.is_pressed:
			os.system('clear')
			clearLCD()
			#screen.fill(black)
			#menuimg = '/home/pi/pokedex/images/Menu.png'
			#menu = pygame.image.load(menuimg).convert_alpha()
			#screen.blit(menu, (0,0))
			#pygame.diplay.update()
			imageLCD('pokeball')
			red.off()
			orange.off()
			blue.off()
			green.on()
			while True:
				pp1 = digit()
				if pp1 == 1:
					break
				elif pp1 == 2:
					os.system('clear')
					clearLCD()
					# pygame.exit()
					sys.exit()
				elif pp1 == 0:
					cameratest()
				else:
					start()
			screen.fill(black)
			bars1 = '/home/pi/pokedex/images/bars.png'
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
			if check >=252:
				blue.off()
				green.off()
				orange.off()
				red.off()
				error2 = '/home/pi/pokedex/images/error.png'
				error = pygame.image.load(error2).convert_alpha()
        		        screen.fill(black)
        	        	screen.blit(error, (0,0))
				pygame.display.update()
				pokeerror = 0
				while pokeerror == 0:
					clearLCD()
					printLCD('ERROR!!!', 0, 0)
					os.system('clear')
					print ("THAT'S NOT A POKEMON!!!")
					print('Press the reset (red) button to go back')
					if button1.is_pressed:
						start()
					red.on()
					time.sleep(0.25)
					red.off()
			pokemon1 = '/home/pi/pokedex/images/' + pokemon2 + '.png'
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
		if button1.is_pressed:
			start()
		screen.fill(black)
        	screen.blit(pokemon, (0,0))
        	pygame.display.update()

clearLCD()
start()
#cameratest()

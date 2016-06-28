from gpiozero import LED
from gpiozero import Button
import time

red = LED(17)
orange = LED(18)
green = LED(19)
blue = LED(10)
button1 = Button(2)
button2 = Button(4)
up = Button(20)
right = Button(21)
down = Button(22)
left = Button(23)

def LEDtest():
	red.on()
	orange.on()
	green.on()
	blue.on()
	time.sleep(10)
	red.off()
	orange.off()
	green.off()
	blue.off()

def BUTTONtest():
	while True:
		if button1.is_pressed:
			print('Button 1')
		elif button2.is_pressed:
			print('Button 2')
		elif up.is_pressed:
			print('Up')
		elif right.is_pressed:
			print('Right')
		elif down.is_pressed:
			print('Down')
		elif left.is_pressed:
			print('Left')
		else:
			print('Nothing')


def start():
        red.on()
        while True:
                if button1.is_pressed:
                        red.off()
                        orange.on()
                        green.on()
                        break
                print("I'm waiting for button")
                if button2.is_pressed:
                        orange.off()
                        red.off()
                        time.sleep(0.5)
                        orange.on()
                        red.on()
                        green.on()
                        print ("Reset")
                        break
                        time.sleep(1)
                        orange.off()
                        green.on()      
                        time.sleep(1)   

BUTTONtest()

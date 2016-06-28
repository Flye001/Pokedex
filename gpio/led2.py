from gpiozero import LED
import time

red = LED(17)
green = LED(18)

while True:
	red.on()
	green.off()
	time.sleep(1)
	red.off()
	green.on()
	time.sleep(1)

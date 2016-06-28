from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=9, green=10, blue=11)

led.blue = 1
sleep(1)
led.blue = 0.5
sleep(1)
led.blue = 0

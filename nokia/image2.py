import time
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI
from PIL import Image

DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))
disp.begin(contrast=30)
disp.clear()
disp.display()

poke1 = raw_input('Enter a Pokemon name: ')
poke = '/home/pi/pokedex/pokes/' + poke1 + '.png'
image = Image.open(poke).convert('1')
disp.image(image)
disp.display()


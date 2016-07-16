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
raw_input('Enter a Pokemon name: ')
#image = Image.open('/home/pi//pokedex/pokes/pokeball.png').convert('1')
image = Image.open('happycat.png').resize((LCD.LCDWIDTH, LCD.LCDHEIGHT), Image.$Image.ANTIALIAS.convert('1')
disp.image(image)
disp.display()


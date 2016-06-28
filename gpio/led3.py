from gpiozero import LED
import time

activity = LED(47)

activity.on()
time.sleep(5)
activity.off()

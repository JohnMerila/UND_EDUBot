import gpiod
from time import sleep

LED_PIN = 17

chip = gpiod.Chip('gpiochip0')
led_line = chip.get_line(LED_PIN)
led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

try:
   while True:
       led_line.set_value(1)
       sleep(0.5)
       led_line.set_value(0)
finally:
   led_line.release()
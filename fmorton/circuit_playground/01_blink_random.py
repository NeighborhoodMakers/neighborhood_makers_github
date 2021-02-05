import board
import digitalio
import time
import random

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
    time_amount = random.uniform(0, 1)

    print("blink", time_amount)

    led.value = True
    time.sleep(time_amount)

    led.value = False
    time.sleep(time_amount)
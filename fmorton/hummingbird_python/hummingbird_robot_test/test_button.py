import time
from HummingbirdLedButton import *

button = HummingbirdLedButton('C', brightness_up = 33, brightness_down = 100)

while True:
    if button.down(1):
        print("BUTTON DOWN")
    else:
        print("BUTTON UP")

    time.sleep(0.05)

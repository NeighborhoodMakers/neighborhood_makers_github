import time
from HummingbirdLedButtons import *

buttons = HummingbirdLedButtons('A')

while True:
    if buttons.down(1):
        print("BUTTON DOWN")
    else:
        print("BUTTON UP")

    time.sleep(0.05)

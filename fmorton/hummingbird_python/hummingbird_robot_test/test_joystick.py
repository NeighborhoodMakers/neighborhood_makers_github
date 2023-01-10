import time
from HummingbirdJoystick import *

joystick = HummingbirdJoystick('B', 0)

joystick.rotation = 2

while True:
    x, y = joystick.values()

    print(x, y)

    time.sleep(0.5)

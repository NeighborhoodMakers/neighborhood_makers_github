import time
from HummingbirdJoystick import *

joystick = HummingbirdJoystick('A', 0)

joystick.rotation = 2

while True:
    x, y = joystick.values()

    print(x, y)

    time.sleep(0.5)

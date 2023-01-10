import time
from HummingbirdJoystick import *
from HummingbirdJoystickCalculator import *

joystick = HummingbirdJoystick('B', 0)
calculator = HummingbirdJoystickCalculator()

joystick.rotation = 3

while True:
    x, y = joystick.values()
    left_speed, right_speed = calculator.car_speeds(x, y)

    print(x, y, left_speed, right_speed)

    time.sleep(0.5)

import time
from HummingbirdJoystickRobot import *
from DoesNotMoveJoystickCalculator import *

#robot = HummingbirdJoystickRobot('A', 'B', joystick_calculator=DoesNotMoveJoystickCalculator())

robot = HummingbirdJoystickRobot('A', 'B', joystick_rotation = 0)

while True:
    robot.move()

    time.sleep(0.05)

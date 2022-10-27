import time
from HummingbirdRobot import *
from DoesNotMoveJoystickCalculator import *

#robot = HummingbirdRobot('A', 'B', joystick_calculator=DoesNotMoveJoystickCalculator())

robot = HummingbirdRobot('A', 'B', joystick_rotation = 0)

while True:
    robot.move()

    time.sleep(0.05)

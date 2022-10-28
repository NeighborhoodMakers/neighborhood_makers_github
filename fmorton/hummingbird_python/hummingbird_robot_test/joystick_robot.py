import time
from HummingbirdRobot import *
from DoesNotMoveJoystickCalculator import *

robot = HummingbirdRobot('A', 'B', 'C', joystick_rotation = 0)
#robot = HummingbirdRobot('A', 'B', joystick_calculator=DoesNotMoveJoystickCalculator())
#robot = HummingbirdRobot(None)

while True:
    robot.move()

    if robot.button_down(1):
        print("RED BUTTON DOWN")

    if robot.button_down(2):
        print("GREEN BUTTON DOWN")

    time.sleep(0.05)

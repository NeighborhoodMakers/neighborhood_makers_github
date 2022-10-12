import time
from HummingbirdJoystickRobot import *

robot = HummingbirdJoystickRobot('A', 'B')

while True:
    robot.move()

    time.sleep(0.05)

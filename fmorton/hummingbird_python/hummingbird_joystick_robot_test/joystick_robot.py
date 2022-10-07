import time
from hummingbird_joystick_robot import *

robot = HummingbirdJoystickRobot('A', 'B')

while True:
    robot.move()

    time.sleep(0.05)

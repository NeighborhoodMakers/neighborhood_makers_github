import time
from HummingbirdRobot import *

robot = HummingbirdRobot('A', 'B', 'C', joystick_rotation = 0)

while True:
    robot.move()

    if robot.button_down(1):
        print("RED BUTTON DOWN")
        time.sleep(3)

    if robot.button_down(2):
        print("GREEN BUTTON DOWN")

    time.sleep(0.05)

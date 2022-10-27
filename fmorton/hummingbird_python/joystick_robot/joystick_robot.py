import time
from HummingbirdRobot import *

robot = HummingbirdRobot('A', 'B')

while True:
    robot.move()

    time.sleep(0.05)

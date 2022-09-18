import time
from hummingbird_robot import *

robot = HummingbirdRobot('A', 'B', 10)

while True:
    robot.move()

    time.sleep(0.05)

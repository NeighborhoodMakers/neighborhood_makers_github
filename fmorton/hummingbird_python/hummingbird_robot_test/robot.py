import time
from hummingbird_robot import *

robot = HummingbirdRobot(motors_device = 'A')

while True:
    robot.move()

    time.sleep(0.05)

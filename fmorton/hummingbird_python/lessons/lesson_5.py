from BirdBrain import Hummingbird
from time import sleep
import random

robot = Hummingbird("A")

# exercise 1
robot.setRotationServo(1, 50)
sleep(1)

# exercise 2
robot.setRotationServo(1, -100)
sleep(2)
robot.setRotationServo(1, 33)
sleep(3)

robot.stopAll()

# exercise 3
for k in range(10):
    robot.setRotationServo(1, -25)
    sleep(0.25)
    robot.setRotationServo(1, 0)
    sleep(0.25)

# exercise 4


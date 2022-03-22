from BirdBrain import Hummingbird
from time import sleep
import random

robot = Hummingbird('A')

robot.setPositionServo(1, 90)

for i in range(5):
    robot.setPositionServo(1, 75)
    sleep(0.33)

    robot.setPositionServo(1, 105)
    sleep(0.33)


for angle in range(180):
    robot.setPositionServo(1, angle)
    #sleep(0.005)

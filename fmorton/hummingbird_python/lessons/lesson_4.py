from BirdBrain import Hummingbird
from time import sleep
import random

robot = Hummingbird("A")

robot.setPositionServo(1, 90)

# exercise 1
for i in range(5):
    robot.setPositionServo(1, 0)
    sleep(0.5)

    robot.setPositionServo(1, 180)
    sleep(0.5)

# exercise 2
for i in range(8):
    robot.setPositionServo(1, 10)
    sleep(0.5)
    robot.setPositionServo(1, 100)
    sleep(0.5)
    robot.setPositionServo(1, 120)
    sleep(0.5)
    robot.setPositionServo(1, 90)
    sleep(0.5)

# exercise 3
for angle in range(180):
    robot.setPositionServo(1, angle)
    sleep(0.1)

# exercise 4
for angle in range(180):
    robot.setPositionServo(1, 180 - angle)
    sleep(0.1)

# exercise 5
for angle_and_brightness in range(100):
    robot.setPositionServo(1, angle_and_brightness)
    robot.setLED(1, angle_and_brightness)

# extra challenge
for k in range(100):
    robot.setPositionServo(1, k * 1.8)
    robot.setLED(1, k)

robot.stopAll()

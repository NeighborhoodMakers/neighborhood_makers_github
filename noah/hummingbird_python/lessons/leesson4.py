from BirdBrain import Hummingbird
from time import sleep

robot = Hummingbird ('A')

for i in range(100):

    robot.setPositionServo(1, i)

for i in range(100):

    robot.setLED(1, i)

    sleep(0.1)


for i in range(100):

    robot.setPositionServo(1, 100-i)

for i in range(100):

    robot.setLED(1, 100-i)

    sleep(0.1)

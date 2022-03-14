from BirdBrain import Hummingbird
from time import sleep

robot = Hummingbird('A')

for k in range(2000):
    robot.setLED(1, 15)
    robot.setLED(2, 40)
    sleep(2.25)

    robot.setLED(1, 0)
    robot.setLED(2, 0)
    sleep(2.25)


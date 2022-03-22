from BirdBrain import Hummingbird
from time import sleep

robot = Hummingbird('A')

# exercise 1
robot.setTriLED(1, 50, 0, 0)
sleep(1)
robot.setTriLED(1, 0, 50, 0)
sleep(1)
robot.setTriLED(1, 0, 0, 50)
sleep(1)
robot.stopAll()

# exercise 2
robot.setTriLED(1, 50, 0, 50)
sleep(1)
robot.setTriLED(1, 0, 50, 50)
sleep(1)
robot.setTriLED(1, 50, 50, 0)
sleep(1)
robot.stopAll()

# exercise 3
for i in range(10):
    robot.setTriLED(1, 0, 50, 0)
    sleep(0.25)
    robot.setTriLED(1, 0, 0, 0)
    sleep(0.25)
robot.setTriLED(1, 50, 0, 0)
sleep(1)
robot.stopAll()

# exercise 4


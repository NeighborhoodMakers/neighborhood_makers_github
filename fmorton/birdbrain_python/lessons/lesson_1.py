from BirdBrain import Hummingbird
from time import sleep

robot = Hummingbird('A')

# exercise 1
robot.setLED(1, 100)
sleep(1)
robot.stopAll()

# exercise 2
robot.setLED(1, 40)
sleep(5)
robot.stopAll()

# exercise 3
robot.setLED(1, 40)
sleep(1)
robot.setLED(1, 0)
robot.setLED(2, 40)
sleep(1)
robot.setLED(2, 0)
robot.setLED(3, 40)
sleep(1)
robot.stopAll()

# exercise 4
robot.setLED(1, 100)
robot.setLED(2, 100)
robot.setLED(3, 100)
sleep(1)
robot.setLED(1, 75)
robot.setLED(2, 75)
robot.setLED(3, 75)
sleep(1)
robot.setLED(1, 50)
robot.setLED(2, 50)
robot.setLED(3, 50)
sleep(1)
robot.setLED(1, 25)
robot.setLED(2, 25)
robot.setLED(3, 25)
sleep(1)
robot.stopAll()

# exercise 4 with a method
def turn_on(intensity):
    robot.setLED(1, intensity)
    robot.setLED(2, intensity)
    robot.setLED(3, intensity)
    sleep(1)

turn_on(100)
turn_on(75)
turn_on(50)
turn_on(25)
robot.stopAll()

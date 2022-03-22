from BirdBrain import Hummingbird
from time import sleep

robot = Hummingbird('A')

robot.setLED(1, 100)

robot.setLED(2,100)

robot.setLED(3,100)

sleep(2)

robot.setLED(1, 75)

robot.setLED(2,75)

robot.setLED(3,75)

sleep(2)

robot.setLED(1,50 )

robot.setLED(2,50)

robot.setLED(3,50)

sleep(2)

robot.setLED(1, 25)

robot.setLED(2,25)

robot.setLED(3,25)

sleep(2)


robot.stopAll()

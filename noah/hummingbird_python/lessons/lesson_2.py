from BirdBrain import Hummingbird
from time import sleep

robot = Hummingbird('A')

robot.setTriLED(1,100,0,0)

sleep(1)

robot.setTriLED(1,0,100,0)

sleep(1)

robot.setTriLED(1,0,0,100)

sleep(1)

robot.setTriLED(1,100,0,100)

sleep(1)

robot.stopAll()

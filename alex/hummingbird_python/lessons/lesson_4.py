from BirdBrain import Hummingbird

from time import sleep

bird = Hummingbird('A')
#
for i in range(180):
    bird.setPositionServo(1,i)
    bird.setLED(1,i)
    sleep(0.1)
for i in range(180):
    bird.setPositionServo(1,180-i)
    bird.setLED(1,100-i)
    sleep(0.1)

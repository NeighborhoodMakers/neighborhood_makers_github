from BirdBrain import Hummingbird

from time import sleep

bird = Hummingbird('A')

bird.setRotationServo(1,100)

sleep(2)

bird.setRotationServo(1,-100)

sleep(3)

bird.stopAll

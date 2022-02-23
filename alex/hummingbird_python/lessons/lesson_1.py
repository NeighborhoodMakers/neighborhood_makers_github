from BirdBrain import Hummingbird

from time import sleep

bird = Hummingbird('A')

bird.setLED(1,100)
bird.setLED(2,100)
bird.setLED(3,100)
sleep(2)
bird.setLED(1,75)
bird.setLED(2,75)
bird.setLED(3,75)
sleep(2)
bird.setLED(1,50)
bird.setLED(2,50)
bird.setLED(3,50)
sleep(2)
bird.setLED(1,25)
bird.setLED(2,25)
bird.setLED(3,25)
sleep(2)

bird.stopAll()

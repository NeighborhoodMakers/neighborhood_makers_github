from BirdBrain import Hummingbird

from time import sleep

bird = Hummingbird('A')
bird.setTriLED(1,100,0,100)
sleep(1)
bird = Hummingbird('A')
bird.setTriLED(1,0,100,100)
sleep(1)
bird = Hummingbird('A')
bird.setTriLED(1,100,100,0)
sleep(1)

bird.stopAll()

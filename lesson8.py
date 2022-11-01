from BirdBrain import Hummingbird
from time import sleep

bird = Hummingbird('A')

#bird.getDistance(1)

threshold = 20
if bird.getDistance(1) < threshold:
    bird.setLED(1, 100)
else:
    bird.setLED(1, 0)
sleep(2)






















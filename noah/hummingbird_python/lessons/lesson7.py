from BirdBrain import Hummingbird
from time import sleep

bird = Hummingbird('A')
print (bird.getLight(1))

threshold = 101

if bird.getLight(1) <threshold:

    bird.setLED(3, 100)

else:
    bird.setLED(3, 0)
    sleep(0.1)




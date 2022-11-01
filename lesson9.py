from BirdBrain import Hummingbird
from time import sleep

bird = Hummingbird('A')

#soundThreshould = 1
#while bird.getSound(2)< soundThreshould:
#    bird.setLED(3,100)
#bird.setLED(3,0)
#sleep(1)

for i in range (232454):
    print(bird.getDial(3))
    bird.setLED(1,bird.getDial(3))




















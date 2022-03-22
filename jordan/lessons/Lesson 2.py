# Imports
from BirdBrain import Hummingbird
from time import sleep

# Declare Hummingbird objects

bird = Hummingbird('A')

# Trilights Exercise 1

#bird.setTriLED(1,100,0,0)
#sleep(1)
#bird.setTriLED(1,0,100,0)
#sleep(1)
#bird.setTriLED(1,0,0,100)
#sleep(1)

# Trilights Exercise 2

#bird.setTriLED(1,100,0,100)
#sleep(1)
#bird.setTriLED(1,0,100,100)
#sleep(1)
#bird.setTriLED(1,100,100,0)
#sleep(1)

#for i in range(10):
#    bird.setTriLED(1,0,100,0)
#    sleep(0.5)
#    bird.setTriLED(1,0,0,0)
#    sleep(0.5)
#
#bird.setTriLED(1,100,0,0)
#sleep(1)

for r in range(6):
    bird.setTriLED(1, 100, 0, 0)
    sleep(1)
    bird.setTriLED(1, 0, 0, 0)
    sleep(1)


for b in range(3):
    bird.setTriLED(1, 0, 0, 100)
    sleep(1)
    bird.setTriLED(1, 0, 0, 0)
    sleep(1)

for g in range(5):
    bird.setTriLED(1, 0, 100, 0)
    sleep(1)
    bird.setTriLED(1, 0, 0, 0)
    sleep(1)

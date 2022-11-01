from BirdBrain import Hummingbird
from time import sleep

bird = Hummingbird('A')

for i in [59, 70, 80, 90 ,100]:
    bird.playNote(i, 0.1)
    sleep(0.1)

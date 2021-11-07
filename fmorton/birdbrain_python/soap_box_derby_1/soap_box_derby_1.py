from BirdBrain import Hummingbird
import time

print("BirdBrain")

robot = Hummingbird('A')

while True:
    distance = robot.getDistance(1)
    print(distance)

    time.sleep(0.1)

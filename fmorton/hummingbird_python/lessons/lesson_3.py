from BirdBrain import Hummingbird
from time import sleep
import random

robot = Hummingbird("A")

# exercise 1
robot.print("FRANK")
# sleep(4)

robot.setDisplay(
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
)
# sleep(1)

# exercise 2
robot.setDisplay(
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0]
)
# sleep(2)

# exercise 3
for i in range(10):
    print("CLICK")
    smile = [0, 1, 0, 1, 0,
             0, 0, 1, 0, 0,
             1, 0, 0, 0, 1,
             0, 1, 1, 1, 0,
             0, 0, 0, 0, 0]
    frown = [0, 1, 0, 1, 0,
             0, 0, 1, 0, 0,
             0, 0, 0, 0, 0,
             0, 1, 1, 1, 0,
             1, 0, 0, 0, 1]

    robot.setDisplay(smile)
    sleep(1)
    robot.setDisplay(frown)
    sleep(1)


pixels = [0] * 25
for times in range(20):
    for i in range(25):
        pixel = random.randint(0, 1)
        # print(pixel)  # decide on k once
        pixels[i] = pixel
        robot.setDisplay(pixels)
    # sleep(1)


robot.stopAll()

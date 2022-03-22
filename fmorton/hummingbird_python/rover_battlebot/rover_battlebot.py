from BirdBrain import Hummingbird
from pygame.locals import *
import time

DISTANCE_TARGET = 150
DISTANCE_SAFE_ZONE_WIDTH = 16
DISTANCE_SAMPLE_MAX = 200.0
DISTANCE_SAMPLE_COUNT = 10         # bigger number means smaller adjustments
DISTANCE_ADJUSTMENT_DIVISOR = 8.0  # bigger number means smaller adjustments
STEER_SERVO_NUMBER = 1
STEER_STRAIGHT = 90
STEER_FREQUENCY_SLEEP = 0.1

pygame.init()

robot = Hummingbird('A')

#robot.setPositionServo(STEER_SERVO_NUMBER, STEER_STRAIGHT)

distance_queue = []

def run():
    print("Running")
    myinput = input()[0]
    print(myinput)

def finish():
    print("Finished")

while True:
    run()
    time.sleep(2)

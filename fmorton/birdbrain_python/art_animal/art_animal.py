from BirdBrain import Hummingbird
from time import sleep
import random

WALK_DELAY = 4.00

def reset(robot):
    setPositionServoWithSleep(robot, 1, 90)
    setPositionServoWithSleep(robot, 2, 90)
    setPositionServoWithSleep(robot, 3, 90)
    sleep(1)

def setPositionServoWithSleep(robot, port, angle):
    robot.setPositionServo(port, angle)
    sleep(0.5)

def walk(robot, port):
    setPositionServoWithSleep(robot, port, 75)
    sleep(WALK_DELAY)
    setPositionServoWithSleep(robot, port, 105)
    sleep(WALK_DELAY)
    setPositionServoWithSleep(robot, port, 90)
    sleep(WALK_DELAY)

def motor_on(robot):
    robot.setLED(1, 30)
    robot.setLED(2, 20)

def motor_off(robot):
    robot.setLED(1, 0)
    robot.setLED(2, 0)

robot = Hummingbird('A')

reset(robot)

for k in range(20):
    #walk(robot, 1)
    #walk(robot, 2)

    motor_on(robot)
    sleep(1)
    motor_off(robot)
    sleep(1)

    print("SPIN")

reset(robot)

robot.stopAll()

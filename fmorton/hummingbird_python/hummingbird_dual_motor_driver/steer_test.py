import pygame

import time
from BirdBrain import Hummingbird
from pygame.locals import *

from hummingbird_dual_motor_driver import *

ROVER_LED_LEFT = 1
ROVER_LED_RIGHT = 2
ROVER_MOTOR_LEFT = 1
ROVER_MOTOR_RIGHT = 2
ROVER_MOTOR_STEERING_WHEEL = 3
ROVER_MOTOR_SPEED = 75
ROVER_DISTANCE_SENSOR = 1

DIRECTION_LEFT = 'L'
DIRECTION_RIGHT = 'R'
DIRECTION_FORWARD = 'F'
DIRECTION_BACKWARD = 'B'
DIRECTION_STOP = 'S'
DIRECTION_STOP_ALL = 'X'

robot = HummingbirdDualMotorDriver('A')
robot_moving = False

pygame.init()


def direction_indicator(direction, speed = 100):
    global robot_moving  # global variables are a horrible practice

    print("Direction is", direction)

    robot_moving = True

    if direction == DIRECTION_LEFT:
        print("Left")
        robot.left_backward(speed)
        robot.right_forward(speed)
    elif direction == DIRECTION_RIGHT:
        print("Right")
        robot.left_forward(speed)
        robot.right_backward(speed)
    elif direction == DIRECTION_FORWARD:
        print("Forward")
        robot.left_forward(speed)
        robot.right_forward(speed)
    elif direction == DIRECTION_BACKWARD:
        print("Backward")
        robot.left_backward(speed)
        robot.right_backward(speed)
    elif direction == DIRECTION_STOP:
        print("Stop")
        robot.left_forward(0)
        robot.right_forward(0)
        robot_moving = False
    elif direction == DIRECTION_STOP_ALL:
        print("Stop All")
        robot.left_forward(0)
        robot.right_forward(0)
        robot_moving = False

def left():
    direction_indicator(DIRECTION_LEFT)

def right():
    direction_indicator(DIRECTION_RIGHT)

def forward():
    direction_indicator(DIRECTION_FORWARD)

def backward():
    direction_indicator(DIRECTION_BACKWARD)

def stop():
    direction_indicator(DIRECTION_STOP)

def stop_all():
    direction_indicator(DIRECTION_STOP_ALL)

def key_down(key):
    if key in [ pygame.K_LEFT, pygame.K_KP4 ]:
        left()
    elif key in [ pygame.K_RIGHT, pygame.K_KP6 ]:
        right()
    elif key in [ pygame.K_UP, pygame.K_KP8 ]:
        forward()
    elif key in [ pygame.K_DOWN, pygame.K_KP2 ]:
        backward()
    elif key in [ pygame.K_5, pygame.K_KP5 ]:
        stop()
    elif key in [ pygame.K_x, pygame.K_RETURN ]:
        stop_all()

def key_up(key):
    pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key_down(event.key)
        elif event.type == pygame.KEYUP:
            key_up(event.key)

        time.sleep(0.05)

# Write your code here :-)

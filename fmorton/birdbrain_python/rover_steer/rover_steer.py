import pygame
import time
from BirdBrain import Hummingbird
from pygame.locals import *

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

rover = Hummingbird('A')
rover_moving = False

pygame.init()

def direction_indicator(direction):
    global rover_moving  # global variables are a horrible practice

    print("Direction is", direction)

    rover_moving = True

    if direction == DIRECTION_LEFT:
        rover.setTriLED(ROVER_LED_LEFT, 0, 100, 0)
        rover.setTriLED(ROVER_LED_RIGHT, 0, 0, 0)
        rover.setRotationServo(ROVER_MOTOR_LEFT, -ROVER_MOTOR_SPEED)
        rover.setRotationServo(ROVER_MOTOR_RIGHT, -ROVER_MOTOR_SPEED)
        rover.setPositionServo(ROVER_MOTOR_STEERING_WHEEL, 140)
    elif direction == DIRECTION_RIGHT:
        rover.setTriLED(ROVER_LED_LEFT, 0, 0, 0)
        rover.setTriLED(ROVER_LED_RIGHT, 0, 100, 0)
        rover.setRotationServo(ROVER_MOTOR_LEFT, ROVER_MOTOR_SPEED)
        rover.setRotationServo(ROVER_MOTOR_RIGHT, ROVER_MOTOR_SPEED)
        rover.setPositionServo(ROVER_MOTOR_STEERING_WHEEL, 40)
    elif direction == DIRECTION_FORWARD:
        rover.setTriLED(ROVER_LED_LEFT, 0, 100, 0)
        rover.setTriLED(ROVER_LED_RIGHT, 0, 100, 0)
        rover.setRotationServo(ROVER_MOTOR_LEFT, ROVER_MOTOR_SPEED)
        rover.setRotationServo(ROVER_MOTOR_RIGHT, -ROVER_MOTOR_SPEED)
        rover.setPositionServo(ROVER_MOTOR_STEERING_WHEEL, 90)
    elif direction == DIRECTION_BACKWARD:
        rover.setTriLED(ROVER_LED_LEFT, 20, 20, 20)
        rover.setTriLED(ROVER_LED_RIGHT, 20, 20, 20)
        rover.setRotationServo(ROVER_MOTOR_LEFT, -ROVER_MOTOR_SPEED)
        rover.setRotationServo(ROVER_MOTOR_RIGHT, ROVER_MOTOR_SPEED)
        rover.setPositionServo(ROVER_MOTOR_STEERING_WHEEL, 90)
    elif direction == DIRECTION_STOP:
        rover.setTriLED(1, 50, 0, 0)
        rover.setTriLED(2, 50, 0, 0)
        rover.setRotationServo(ROVER_MOTOR_LEFT, 0)
        rover.setRotationServo(ROVER_MOTOR_RIGHT, 0)
        rover.setPositionServo(ROVER_MOTOR_STEERING_WHEEL, 90)
        rover_moving = False
    elif direction == DIRECTION_STOP_ALL:
        rover.setTriLED(1, 0, 0, 0)
        rover.setTriLED(2, 0, 0, 0)
        rover.setRotationServo(ROVER_MOTOR_LEFT, 0)
        rover.setRotationServo(ROVER_MOTOR_RIGHT, 0)
        rover.setPositionServo(ROVER_MOTOR_STEERING_WHEEL, 90)
        rover_moving = False

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
    elif key in [ pygame.K_x ]:
        stop_all()

def key_up(key):
    pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key_down(event.key)
        elif event.type == pygame.KEYUP:
            key_up(event.key)

    if rover_moving and rover.getDistance(ROVER_DISTANCE_SENSOR) < 20:
        print("Avoid Problem")

        backward()
        time.sleep(1)

        left()
        time.sleep(1)

        forward()
    else:
        time.sleep(0.05)

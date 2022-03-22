from BirdBrain import Hummingbird
from time import sleep
import random

WALK_DELAY = 4.00

def reset(robot):
    robot.stopAll()

    set_position_servo_with_sleep(robot, 1, 90)
    set_position_servo_with_sleep(robot, 2, 90)
    set_position_servo_with_sleep(robot, 3, 90)
    sleep(1)

def set_position_servo_with_sleep(robot, port, angle):
    robot.setPositionServo(port, angle)
    sleep(0.5)

def walk(robot, port):
    set_position_servo_with_sleep(robot, port, 75)
    sleep(WALK_DELAY)
    set_position_servo_with_sleep(robot, port, 105)
    sleep(WALK_DELAY)
    set_position_servo_with_sleep(robot, port, 90)
    sleep(WALK_DELAY)

def motor_on(robot):
    robot.setLED(1, 40)
    robot.setLED(2, 20)

def motor_off(robot):
    robot.setLED(1, 0)
    robot.setLED(2, 0)

def move(robot, red, green, blue, sleep_amount):
    set_position_servo_with_sleep(robot, 1, red)
    set_position_servo_with_sleep(robot, 2, green)
    set_position_servo_with_sleep(robot, 3, blue)
    motor_on(robot)
    sleep(sleep_amount)
    motor_off(robot)

def move_forward(robot, sleep_amount):
    move(robot, 110, 70, 90, sleep_amount)

def move_left(robot, sleep_amount):
    move(robot, 90, 40, 70, sleep_amount)

def move_right(robot, sleep_amount):
    move(robot, 90, 120, 130, sleep_amount)

def move_backward(robot, sleep_amount):
    move(robot, 50, 140, 90, sleep_amount)

robot = Hummingbird('A')

reset(robot)

# the front of the robot is where the spinning motor is located
# straight = 110, 70, 90
# left 90, 40, 70
# right 90, 120, 130
# backwards 50, 140, 90

for k in range(20):
    #move(robot, 50, 140, 90, 2)

    move_forward(robot, 2)
    move_left(robot, 2)
    move_backward(robot, 5)

    #walk(robot, 1)
    #walk(robot, 2)

    #motor_on(robot)
    #sleep(1)
    #motor_off(robot)
    #sleep(1)

    print("MOVE")

reset(robot)

robot.stopAll()

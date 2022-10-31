import threading
import time
from HummingbirdRobot import *

def move_robot(robot):
    while True:
        robot.move()

def red_button_down(robot):
    print("RED BUTTON DOWN")

def green_button_down(robot):
    print("GREEN BUTTON DOWN")

robot = HummingbirdRobot('A', 'B', 'C', joystick_rotation = 0)

joystick_thread = threading.Thread(target=move_robot, args=(robot,))
joystick_thread.start()

while True:
    if robot.button_down(1):
        threading.Thread(target=red_button_down, args=(robot,)).start()

    if robot.button_down(2):
        threading.Thread(target=green_button_down, args=(robot,)).start()

    time.sleep(0.05)


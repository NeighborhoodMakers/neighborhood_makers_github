import time
from hummingbird_joystick_robot import *
from does_not_move_joystick_calculator import *

#robot = HummingbirdJoystickRobot('A', 'B', joystick_calculator=DoesNotMoveJoystickCalculator())

robot = HummingbirdJoystickRobot('A', 'B', joystick_rotation = 0)

while True:
    robot.move()

    time.sleep(0.05)

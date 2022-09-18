import time
from BirdBrain import Hummingbird
#from pygame.locals import *

from hummingbird_dual_motor_driver import *
from hummingbird_joystick import *

class HummingbirdRobot:
    def __init__(self, joy_stick_device = 'A', motors_device = 'B'):
        self.joy_stick_device = joy_stick_device
        self.motors_device = motors_device

        self.joy_stick = HummingbirdJoyStick(self.joy_stick_device)
        self.motors = None
        self.motors = HummingbirdDualMotorDriver(self.motors_device, 40)


robot = HummingbirdRobot('A', 'B')

NOT_MOVING_WINDOW = 20.0
STRAIGHT_WINDOW_SIZE = 33.0
FORWARD_TURN_MULTIPLIER = 0.75
BACKWARD_TURN_MULTIPLIER = 0.33

def speeds(x, y):
    speed = max(abs(x), abs(y))
    speed_multiplier = speed / 100.0

    #print(x, y, speed, speed_multiplier)
    if abs(y) < NOT_MOVING_WINDOW:
        return(0, 0)

    if abs(x) <= STRAIGHT_WINDOW_SIZE:
        if y > 0:
            # straight forward
            print("straight forward", x, y)
            return(speed, speed)
        else:
            # straight backwards
            print("straight backwards", x, y)
            return(-speed, -speed)
    elif x < 0:
        # left
        if y < 0:
            # left backwards
            print("left backwards", x, y)
            return(-speed * BACKWARD_TURN_MULTIPLIER, -speed)
            #return(x * speed_multiplier, y * speed_multiplier)
        else:
            # left forward
            print("left forward", x, y)
            return(-speed * FORWARD_TURN_MULTIPLIER, speed)
    else:
        # right
        if y < 0:
            # right backwards
            print("right backwards", x, y)
            return(-speed, -speed * BACKWARD_TURN_MULTIPLIER)
            #return(y * speed_multiplier, -x * speed_multiplier)
        else:
            # right forward
            print("right forward", x, y)
            return(speed, -speed * FORWARD_TURN_MULTIPLIER)
            #return(y * speed_multiplier, x * speed_multiplier)

    return(0, 0)

while True:
    x,y = robot.joy_stick.values()
    time.sleep(0.05)
    robot.motors.move(speeds(x, y))

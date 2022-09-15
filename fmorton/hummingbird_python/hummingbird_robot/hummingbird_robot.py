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
        self.motors = HummingbirdDualMotorDriver(self.motors_device, 40)


robot = HummingbirdRobot('A', 'B')

while True:
    x,y = robot.joy_stick.values()
    print("ROBOT SPEED and DIRECTION", x, y)
    time.sleep(0.05)
    robot.motors.move(x, x)

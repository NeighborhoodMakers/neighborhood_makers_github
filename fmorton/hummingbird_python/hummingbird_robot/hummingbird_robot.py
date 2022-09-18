import time
from BirdBrain import Hummingbird
#from pygame.locals import *

from hummingbird_dual_motor_driver import *
from hummingbird_joy_stick import *
from hummingbird_joy_stick_calculator import *

class HummingbirdRobot:
    def __init__(self, joy_stick_device = 'A', motors_device = 'B'):
        self.joy_stick_device = joy_stick_device
        self.motors_device = motors_device

        self.joy_stick = HummingbirdJoyStick(self.joy_stick_device)
        self.joy_stick_calculator = HummingbirdJoyStickCalculator()
        self.motors = HummingbirdDualMotorDriver(self.motors_device, 40)

    def move(self):
        x,y = robot.joy_stick.values()

        robot.motors.move(robot.joy_stick_calculator.speeds(x, y))


robot = HummingbirdRobot('A', 'B')

while True:
    robot.move()

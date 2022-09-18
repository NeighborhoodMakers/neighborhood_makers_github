import time
from BirdBrain import Hummingbird
#from pygame.locals import *

from hummingbird_dual_motor_driver import *
from hummingbird_joy_stick import *
from hummingbird_joy_stick_calculator import *

class HummingbirdRobot:
    def __init__(self, joy_stick_device = 'A', motors_device = 'B', minimum_motor_speed = HummingbirdDualMotorDriver.MINIMUM_SPEED):
        self.joy_stick_device = joy_stick_device
        self.motors_device = motors_device
        self.minimum_motor_speed = minimum_motor_speed

        self.joy_stick = HummingbirdJoyStick(self.joy_stick_device)
        self.joy_stick_calculator = HummingbirdJoyStickCalculator()
        self.motors = HummingbirdDualMotorDriver(self.motors_device, self.minimum_motor_speed)

    def move(self):
        x,y = self.joy_stick.values()

        self.motors.move(self.joy_stick_calculator.speeds(x, y))

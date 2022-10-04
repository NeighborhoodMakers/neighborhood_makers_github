import time
from BirdBrain import Hummingbird
#from pygame.locals import *

from hummingbird_dual_motor_driver import *
from hummingbird_joy_stick import *
from hummingbird_joy_stick_calculator import *

class HummingbirdRobot:
    def __init__(self, motors_device = 'A', joy_stick_device = 'B', minimum_motor_speed = None):
        self.motors_device = motors_device
        self.joy_stick_device = joy_stick_device
        self.minimum_motor_speed = HummingbirdDualMotorDriver.MINIMUM_SPEED if minimum_motor_speed is None else minimum_motor_speed

        self.joy_stick = None
        self.joy_stick_calculator = HummingbirdJoyStickCalculator()
        self.motors = HummingbirdDualMotorDriver(self.motors_device, self.minimum_motor_speed)

        self.joy_stick = None if self.joy_stick_device is not None else HummingbirdJoyStick(self.joy_stick_device)
        self.joy_stick_calculator = HummingbirdJoyStickCalculator()
        self.motors = None if self.motors_device is not None else HummingbirdDualMotorDriver(self.motors_device, self.minimum_motor_speed)

    def move(self):
        x,y = self.joy_stick.values()

        self.motors.move(self.joy_stick_calculator.speeds(x, y))

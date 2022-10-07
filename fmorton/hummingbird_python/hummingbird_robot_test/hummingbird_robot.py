import time
from BirdBrain import Hummingbird
#from pygame.locals import *

from hummingbird_dual_motor_driver import *
from hummingbird_joy_stick import *
from hummingbird_joy_stick_calculator import *

class HummingbirdRobot:
    def __init__(self, motors_device = None, joy_stick_device = None, minimum_motor_speed = None):
        self.motors_device = motors_device
        self.joy_stick_device = joy_stick_device
        if minimum_motor_speed is None: self.minimum_motor_speed = HummingbirdDualMotorDriver.MINIMUM_SPEED

        self.motors = None
        self.joy_stick = None
        self.joy_stick = None

        if self.motors_device is not None:
            self.motors = HummingbirdDualMotorDriver(self.motors_device, self.minimum_motor_speed)

        if self.joy_stick_device is not None:
            self.joy_stick = None if self.joy_stick_device is not None else HummingbirdJoyStick(self.joy_stick_device)
            self.joy_stick_calculator = HummingbirdJoyStickCalculator()

    def move_speed_from_joystick(self):
        if self.joy_stick is None:
            return([0, 0])
        else:
            x, y = self.joy_stick.values()
            return(self.joy_stick_calculator.speeds(x, y))

    def move_speed(self):
        move_from_joystick()

    def move(self):
        if self.motors is not None:
            self.motors.move(move_speed_from_joystick())

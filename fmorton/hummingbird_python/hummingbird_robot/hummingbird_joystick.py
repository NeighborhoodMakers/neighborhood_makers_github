from BirdBrain import Hummingbird
import time

class HummingbirdJoyStick:
    ZERO_MARGIN = 0.02
    ZERO_MAX = 3.0
    ZERO_MIN = 0.0
    ZERO_BIAS = 1.25

    def __init__(self, device = 'A'):
        self.device = device
        self.joy_stick = Hummingbird(device)

        self.calibrate()

    def calibrate(self):
        self.button_base = round(self.joy_stick.getVoltage(1), 2)
        self.x_base = round(self.joy_stick.getVoltage(3), 2)
        self.y_base = round(self.joy_stick.getVoltage(2), 2)

    def joystick_round(self, value, base):
        if (value > (base - self.ZERO_MARGIN)) and (value < (base + self.ZERO_MARGIN)):
            return(0)

        normalized_value = (100 - ((3.0 - value) / ((3.0 - base) / 100))) * self.ZERO_BIAS

        if normalized_value < -100.0:
            return(-100.0)

        if normalized_value > 100:
            return(100)

        return(round(normalized_value, 2))

    def values(self):
        button = self.joystick_round(self.joy_stick.getVoltage(1), self.button_base)
        x = self.joystick_round(self.joy_stick.getVoltage(3), self.x_base)
        y = self.joystick_round(self.joy_stick.getVoltage(2), self.y_base)

        return(x, y)

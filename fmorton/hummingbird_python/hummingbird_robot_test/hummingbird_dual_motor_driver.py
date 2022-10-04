from BirdBrain import Hummingbird
import time

class HummingbirdDualMotorDriver:
    MINIMUM_SPEED = 30

    def __init__(self, device = 'A', minimum_speed = MINIMUM_SPEED):
        self.device = device
        self.minimum_speed = minimum_speed

        self.left_polarity = 1
        self.right_polarity = 1

        self.robot = Hummingbird(device)

    def reverse_left_polarity(self):
        self.left_polarity = -self.left_polarity

    def reverse_right_polarity(self):
        self.right_polarity = -self.right_polarity

    def adjust_speed_for_polarity(self, speed, multiplier):
        return(speed * multiplier)

    def move_left_motor(self, speed):
        speed = self.adjust_speed_for_polarity(speed, self.left_polarity)

        if speed == 0 or (abs(speed) < self.minimum_speed):
            self.robot.setTriLED(1, 0, 0, 0)
        elif speed > 0:
            self.robot.setTriLED(1, abs(speed), 100, 0)
        else:
            self.robot.setTriLED(1, abs(speed), 0, 100)

    def move_right_motor(self, speed):
        speed = self.adjust_speed_for_polarity(speed, self.right_polarity)

        if speed == 0 or (abs(speed) < self.minimum_speed):
            self.robot.setTriLED(2, 0, 0, 0)
        elif speed > 0:
            self.robot.setTriLED(2, 0, 100, abs(speed))
        else:
            self.robot.setTriLED(2, 100, 0, abs(speed))

    def move(self, left_speed, right_speed = None):
        if type(left_speed) is list:
            left_speed, right_speed = left_speed

        self.move_left_motor(left_speed)
        self.move_right_motor(right_speed)

    def stop(self):
        self.robot.setTriLED(1, 0, 0, 0)
        self.robot.setTriLED(2, 0, 0, 0)

    def stop_all(self):
        self.stop()
        self.robot.stopAll()

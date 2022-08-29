from BirdBrain import Hummingbird
import time

class HummingbirdDualMotorDriver:
    def __init__(self, device = 'A'):
        self.robot = Hummingbird(device)

    def left_forward(self, speed):
        self.robot.setTriLED(1, speed, 100, 0)

    def right_forward(self, speed):
        self.robot.setTriLED(2, 0, 100, speed)

    def left_backward(self, speed):
        self.robot.setTriLED(1, speed, 0, 100)

    def right_backward(self, speed):
        self.robot.setTriLED(2, 100, 0, speed)

    def stop(self):
        self.robot.setTriLED(1, 0, 0, 0)
        self.robot.setTriLED(2, 0, 0, 0)

    def stop_all(self):
        self.stop()
        self.robot.stopAll()

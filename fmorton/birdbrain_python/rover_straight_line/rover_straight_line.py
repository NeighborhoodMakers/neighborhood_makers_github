from BirdBrain import Hummingbird
import time

ROVER_MOTOR_LEFT = 1
ROVER_MOTOR_RIGHT = 2

rover = Hummingbird('A')

rover.setTriLED(1, 0, 100, 0)
rover.setTriLED(2, 0, 100, 0)

rover.setRotationServo(ROVER_MOTOR_LEFT, 40 * 1.00)
rover.setRotationServo(ROVER_MOTOR_RIGHT, -40 * 1.15)

time.sleep(4)

rover.setTriLED(1, 0, 100, 0)
rover.setTriLED(2, 0, 100, 0)

time.sleep(1)

rover.stopAll()

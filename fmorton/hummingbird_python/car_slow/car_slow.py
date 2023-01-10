import time
from BirdBrain import Hummingbird
from HummingbirdJoystick import *
from CarJoystickCalculator import *

LEFT = 1
RIGHT = 2

#robot = Hummingbird('A')
#joystick = HummingbirdJoystick('B', 3)
calculator = CarJoystickCalculator()

for k in range(5):
    robot.setRotationServo(LEFT, 100)
    robot.setRotationServo(RIGHT, 50)
    print("pass ", k)
    time.sleep(0.5)


while True:
    x, y = joystick.values()
    left_speed, right_speed = calculator.car_speeds(x, y)

    print("Running ", x, y, left_speed, right_speed)

    print(x, y)

    robot.setRotationServo(LEFT, right_speed)
    robot.setRotationServo(RIGHT, left_speed)

    #time.sleep(0.1)

    #robot.setRotationServo(LEFT, 0)
    #robot.setRotationServo(RIGHT, 0)
    #time.sleep(0.5)

from BirdBrain import Hummingbird
import time

ZERO_MARGIN = 0.02
ZERO_MAX = 3.0
ZERO_MIN = 0.0
ZERO_BIAS = 1.25

def joystick_round(value, base):
    if (value > (base - ZERO_MARGIN)) and (value < (base + ZERO_MARGIN)):
        return(0)

    normalized_value = (100 - ((3.0 - value) / ((3.0 - base) / 100))) * ZERO_BIAS

    if normalized_value < -100.0:
        return(-100.0)

    if normalized_value > 100:
        return(100)

    return(round(normalized_value, 2))

robot = Hummingbird('A')

button_base = round(robot.getVoltage(1), 2)
x_base = round(robot.getVoltage(3), 2)
y_base = round(robot.getVoltage(2), 2)

while True:
    button = joystick_round(robot.getVoltage(1), button_base)
    x = joystick_round(robot.getVoltage(3), x_base)
    y = joystick_round(robot.getVoltage(2), y_base)

    print(x, y)

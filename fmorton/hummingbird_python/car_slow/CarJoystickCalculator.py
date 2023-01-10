from HummingbirdJoystickCalculator import *

class CarJoystickCalculator(HummingbirdJoystickCalculator):
    def straight_back(self, speed, x, y):
        return(-speed, -speed)

    def straight_forward(self, speed, x, y):
        return(speed, speed)

    def left_back(self, speed, x, y):
        return(-speed * HummingbirdJoystickCalculator.BACKWARD_TURN_MULTIPLIER, -speed)

    def left_forward(self, speed, x, y):
        return(-speed * HummingbirdJoystickCalculator.FORWARD_TURN_MULTIPLIER, speed)

    def right_back(self, speed, x, y):
        return(-speed, -speed * HummingbirdJoystickCalculator.BACKWARD_TURN_MULTIPLIER)

    def right_forward(self, speed, x, y):
        return(speed, -speed * HummingbirdJoystickCalculator.FORWARD_TURN_MULTIPLIER)

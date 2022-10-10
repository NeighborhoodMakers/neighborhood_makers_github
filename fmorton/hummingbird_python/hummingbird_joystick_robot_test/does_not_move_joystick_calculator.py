from hummingbird_joystick_calculator import *

class DoesNotMoveJoystickCalculator(HummingbirdJoystickCalculator):
    def speeds(self, x, y):
        print("Not moving", x, y)

        return(0, 0)

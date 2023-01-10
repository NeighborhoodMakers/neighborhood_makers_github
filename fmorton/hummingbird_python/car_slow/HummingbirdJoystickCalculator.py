class HummingbirdJoystickCalculator:
    NOT_MOVING_WINDOW_SIZE = 20.0
    STRAIGHT_WINDOW_SIZE = 25.0
    FORWARD_TURN_MULTIPLIER = 0.75
    BACKWARD_TURN_MULTIPLIER = 0.33
    BACKWARD_TURN_MULTIPLIER = 0.75

    def track_speeds(self, x, y):
        print("DEBUG: USING THE NEW ONE")
        speed = max(abs(x), abs(y))

        if speed < HummingbirdJoystickCalculator.NOT_MOVING_WINDOW_SIZE:
            return(0, 0)

        if abs(x) <= HummingbirdJoystickCalculator.STRAIGHT_WINDOW_SIZE:
            if y > 0:
                # straight forward
                return(speed, speed)
            else:
                # straight backwards
                return(-speed, -speed)
        elif x < 0:
            if y < 0:
                # left backwards
                return(-speed * HummingbirdJoystickCalculator.BACKWARD_TURN_MULTIPLIER, -speed)
            else:
                # left forward
                return(-speed * HummingbirdJoystickCalculator.FORWARD_TURN_MULTIPLIER, speed)
        else:
            if y < 0:
                # right backwards
                return(-speed, -speed * HummingbirdJoystickCalculator.BACKWARD_TURN_MULTIPLIER)
            else:
                # right forward
                return(speed, -speed * HummingbirdJoystickCalculator.FORWARD_TURN_MULTIPLIER)

        return(0, 0)

    def car_speeds(self, x, y):
        print("DEBUG: USING THE NEW ONE")
        speed = max(abs(x), abs(y))
        print("DEBUG: speed is ", speed)

        TURN_DIVISOR = 3

        if speed < HummingbirdJoystickCalculator.NOT_MOVING_WINDOW_SIZE:
            return(0, 0)

        if y > 0:
            if x > 0:
                # right forward
                print("turn right for calculations ", speed, abs(x))
                left_speed = speed
                right_speed = max((speed - abs(x)) * 1.0, 50)
                #right_speed = max(right_speed, 50)
            else:
                # left forward
                print("turn left for calculations ", speed, abs(x))
                left_speed = max((speed - abs(x)) * 1.0, 50)
                right_speed = speed
                #left_speed = max(left_speed, 50)
        else:
            if x > 0:
                # right backwards
                left_speed = -100
                right_speed = -100
            else:
                # left backwards
                left_speed = -100
                right_speed = -100

        return(left_speed, right_speed)

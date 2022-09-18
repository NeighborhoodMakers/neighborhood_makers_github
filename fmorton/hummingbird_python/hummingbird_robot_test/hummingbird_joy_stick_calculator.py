class HummingbirdJoyStickCalculator:
    NOT_MOVING_WINDOW_SIZE = 20.0
    STRAIGHT_WINDOW_SIZE = 25.0
    FORWARD_TURN_MULTIPLIER = 0.75
    BACKWARD_TURN_MULTIPLIER = 0.33

    def speeds(self, x, y):
        speed = max(abs(x), abs(y))

        if abs(y) < HummingbirdJoyStickCalculator.NOT_MOVING_WINDOW_SIZE:
            return(0, 0)

        if abs(x) <= HummingbirdJoyStickCalculator.STRAIGHT_WINDOW_SIZE:
            if y > 0:
                # straight forward
                return(speed, speed)
            else:
                # straight backwards
                return(-speed, -speed)
        elif x < 0:
            if y < 0:
                # left backwards
                return(-speed * HummingbirdJoyStickCalculator.BACKWARD_TURN_MULTIPLIER, -speed)
            else:
                # left forward
                return(-speed * HummingbirdJoyStickCalculator.FORWARD_TURN_MULTIPLIER, speed)
        else:
            if y < 0:
                # right backwards
                return(-speed, -speed * HummingbirdJoyStickCalculator.BACKWARD_TURN_MULTIPLIER)
            else:
                # right forward
                return(speed, -speed * HummingbirdJoyStickCalculator.FORWARD_TURN_MULTIPLIER)

        return(0, 0)

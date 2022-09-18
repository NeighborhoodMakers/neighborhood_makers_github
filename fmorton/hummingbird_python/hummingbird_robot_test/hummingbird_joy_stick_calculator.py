class HummingbirdJoyStickCalculator:
    NOT_MOVING_WINDOW = 20.0
    STRAIGHT_WINDOW_SIZE = 25.0
    FORWARD_TURN_MULTIPLIER = 0.75
    BACKWARD_TURN_MULTIPLIER = 0.33

    def speeds(self, x, y):
        speed = max(abs(x), abs(y))
        speed_multiplier = speed / 100.0

        #print(x, y, speed, speed_multiplier)
        if abs(y) < HummingbirdJoyStickCalculator.NOT_MOVING_WINDOW:
            return(0, 0)

        if abs(x) <= HummingbirdJoyStickCalculator.STRAIGHT_WINDOW_SIZE:
            if y > 0:
                # straight forward
                print("straight forward", x, y)
                return(speed, speed)
            else:
                # straight backwards
                print("straight backwards", x, y)
                return(-speed, -speed)
        elif x < 0:
            # left
            if y < 0:
                # left backwards
                print("left backwards", x, y)
                return(-speed * HummingbirdJoyStickCalculator.BACKWARD_TURN_MULTIPLIER, -speed)
                #return(x * speed_multiplier, y * speed_multiplier)
            else:
                # left forward
                print("left forward", x, y)
                return(-speed * HummingbirdJoyStickCalculator.FORWARD_TURN_MULTIPLIER, speed)
        else:
            # right
            if y < 0:
                # right backwards
                print("right backwards", x, y)
                return(-speed, -speed * HummingbirdJoyStickCalculator.BACKWARD_TURN_MULTIPLIER)
                #return(y * speed_multiplier, -x * speed_multiplier)
            else:
                # right forward
                print("right forward", x, y)
                return(speed, -speed * HummingbirdJoyStickCalculator.FORWARD_TURN_MULTIPLIER)
                #return(y * speed_multiplier, x * speed_multiplier)

        return(0, 0)

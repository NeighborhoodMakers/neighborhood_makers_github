import time
from BirdBrain import Finch
from hummingbird_dual_motor_driver import *

motors = HummingbirdDualMotorDriver('A')

motors.move([ -50, -50 ])

time.sleep(1)

motors.move([ 0, 0 ])

time.sleep(1)


motors.move(0, 50)

time.sleep(1)

motors.move(0, 0)

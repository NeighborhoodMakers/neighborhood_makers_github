import time
from BirdBrain import Hummingbird
from hummingbird_dual_motor_driver import *

#robot = Hummingbird('A')

motors = HummingbirdDualMotorDriver()

motors.move([ -50, -50 ])
time.sleep(1)

motors.move([ 0, 0 ])
time.sleep(1)

motors.move(0, 50)
time.sleep(1)

motors.move(0, 0)

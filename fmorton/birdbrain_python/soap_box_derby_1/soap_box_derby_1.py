from BirdBrain import Hummingbird
import time

DISTANCE_TARGET = 150
DISTANCE_SAFE_ZONE_WIDTH = 16
DISTANCE_SAMPLE_MAX = 200.0
DISTANCE_SAMPLE_COUNT = 10         # bigger number means smaller adjustments
DISTANCE_ADJUSTMENT_DIVISOR = 8.0  # bigger number means smaller adjustments
STEER_SERVO_NUMBER = 1
STEER_STRAIGHT = 90
STEER_FREQUENCY_SLEEP = 0.1

robot = Hummingbird('A')

robot.setPositionServo(STEER_SERVO_NUMBER, STEER_STRAIGHT)

distance_queue = []

while True:
    #----------------------------------------------------------------------------------------------
    #  get current distance from railing and ignore if unreasonable
    #----------------------------------------------------------------------------------------------
    distance_sample = robot.getDistance(1)

    if distance_sample > DISTANCE_SAMPLE_MAX: continue

    #----------------------------------------------------------------------------------------------
    #  get a moving average of the distance from the railing
    #----------------------------------------------------------------------------------------------
    if len(distance_queue) >= DISTANCE_SAMPLE_COUNT: distance_queue.pop(0)

    distance_queue.append(distance_sample)

    distance = sum(distance_queue) / len(distance_queue)

    distance_off_of_center = DISTANCE_TARGET - distance

    #----------------------------------------------------------------------------------------------
    #  go straight if in the center of the distance window
    #----------------------------------------------------------------------------------------------
    if abs(distance_off_of_center) <= DISTANCE_SAFE_ZONE_WIDTH:
        print('straight')
        robot.setPositionServo(STEER_SERVO_NUMBER, STEER_STRAIGHT)
        continue

    #----------------------------------------------------------------------------------------------
    #  adjust steering
    #----------------------------------------------------------------------------------------------
    distance_adjustment = distance_off_of_center / DISTANCE_ADJUSTMENT_DIVISOR

    steering_adjustment = STEER_STRAIGHT - distance_adjustment

    print(distance_queue, '-->', distance, ' off=', distance_off_of_center," adjust=",distance_adjustment, '  new angle is.............. ',steering_adjustment)

    robot.setPositionServo(STEER_SERVO_NUMBER, steering_adjustment)

    time.sleep(STEER_FREQUENCY_SLEEP)

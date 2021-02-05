import time
import makers_motor_control
import makers_remote_control
from adafruit_crickit import crickit

motors = makers_motor_control.MotorControl()
remote_control = makers_remote_control.RemoteControl()
servo = crickit.servo_1

motors.set_throttle(0.0, 0.0)
servo.angle = 0

while True:
    code = remote_control.code()

    if(code == remote_control.CODE_UP):
        print("Forward")
        motors.set_throttle(0.5, 0.5, 2.25, True)
    elif(code == remote_control.CODE_DOWN):
        print("Backwards")
        motors.set_throttle(-0.5, -0.5, 2.25, True)
    elif(code == remote_control.CODE_LEFT):
        print("Left")
        motors.set_throttle(0.0, 0.5, 1.25, True)
    elif(code == remote_control.CODE_RIGHT):
        print("Right")
        motors.set_throttle(0.5, 0.0, 1.25, True)
    elif(code == remote_control.CODE_STOP_MODE) or (code == remote_control.CODE_ENTER):
        print("Stop")
        motors.set_throttle(0.0, 0.0)
    elif(code == 4):
        print("Up")
        servo.angle = 180
    elif(code == 6):
        print("Down")
        servo.angle = 0

    time.sleep(0.2)
import time
import board
#import neopixel
import makers_motor_control
import makers_remote_control
#from adafruit_crickit import crickit
import hard_hat_neo_pixels

#motors = makers_motor_control.MotorControl()
remote_control = makers_remote_control.RemoteControl(debug=False)
#servo = crickit.servo_1
neo_pixels = hard_hat_neo_pixels.HardHatNeoPixels(43)

#motors.set_throttle(0.0, 0.0)
#servo.angle = 0

while True:
    #neo_pixels.fill(neo_pixels.NOTHING)

    code = remote_control.code(blocking=True)

    print ("the code is", code)

    if(code == remote_control.UP_):
        print("Forward")
        neo_pixels.fill(neo_pixels.GREEN)
        #motors.set_throttle(0.5, 0.5, 0.25, True)
    #elif(code == remote_control.DOWN):
    #    #print("Backwards")
    #    #motors.set_throttle(-0.5, -0.5, 0.25, True)
    #    pass
    #elif(code == remote_control.LEFT):
    #    #print("Left")
    #    #motors.set_throttle(0.0, 0.5, 0.25, True)
    #    pass
    #elif(code == remote_control.RIGHT):
    #    #print("Right")
    #    #motors.set_throttle(0.5, 0.0, 0.25, True)
    #    pass
    elif(code == remote_control.STOP) or (code == remote_control.ENTER):
        print("Stop")
        neo_pixels.fill(neo_pixels.YELLOW)
       #motors.set_throttle(0.0, 0.0)
    elif(code == 0):
        neo_pixels.fill(neo_pixels.NOTHING)
        time.sleep(1.0)

    elif(code == 1):
        neo_pixels.fill(neo_pixels.PURPLE)
    #elif(code == 4):
    #    print("Up")
    #    servo.angle = 180

    print("DEBUG: idle.....")
    neo_pixels.idle(neo_pixels.WHITE)
    print("DEBUG: idle.....done")

    time.sleep(0.1)

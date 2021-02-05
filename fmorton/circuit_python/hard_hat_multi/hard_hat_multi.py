import time
import board
import adafruit_irremote
#import neopixel
#import makers_motor_control
import makers_remote_control
#from adafruit_crickit import crickit
import hard_hat_animated_neo_pixels

#motors = makers_motor_control.MotorControl()
remote_control = makers_remote_control.RemoteControl(debug=False)
#servo = crickit.servo_1
neo_pixels = hard_hat_animated_neo_pixels.HardHatAnimatedNeoPixels(43)

neo_pixels.fill(neo_pixels.NOTHING)

#motors.set_throttle(0.0, 0.0)
#servo.angle = 0

use_random_color = True
color = neo_pixels.NOTHING

red = 255
green = 255
blue = 255

while True:
    try:
        code = remote_control.code(blocking=False)

        print("code is", code)
        if(code == remote_control.CODE_UP):
            neo_pixels.fill(neo_pixels.BLUE)
        #    #motors.set_throttle(0.5, 0.5, 0.25, True)
        #elif(code == remote_control.CODE_DOWN):
        #    #print("Backwards")
        #    #motors.set_throttle(-0.5, -0.5, 0.25, True)
        #    pass
        #elif(code == remote_control.CODE_LEFT):
        #    #print("Left")
        #    #motors.set_throttle(0.0, 0.5, 0.25, True)
        #    pass
        #elif(code == remote_control.CODE_RIGHT):
        #    #print("Right")
        #    #motors.set_throttle(0.5, 0.0, 0.25, True)
        #    pass
        #elif(code == remote_control.CODE_STOP_MODE) or (code == remote_control.CODE_ENTER):
        #    print("Stop")
        #    neo_pixels.fill(neo_pixels.YELLOW)
        #   #motors.set_throttle(0.0, 0.0)
        #elif(code == 0):
        #    neo_pixels.fill(neo_pixels.NOTHING)
        #    time.sleep(1.0)
        #elif(code == 1):
        #    neo_pixels.fill(neo_pixels.PURPLE)
        #elif(code == 4):
        #    print("Up")
        #    servo.angle = 180
        elif(code == 4):
            neo_pixels.fill(neo_pixels.RED)
            red = 0
            green = 255
            blue = 255
        elif(code == 5):
            neo_pixels.fill(neo_pixels.GREEN)
            red = 255
            green = 0
            blue = 255
        elif(code == 6):
            neo_pixels.fill(neo_pixels.BLUE)
            red = 255
            green = 255
            blue = 0

        if use_random_color:
            color = neo_pixels.random_color(max_red=red, max_blue=blue, max_green=green)

        neo_pixels.color(color)
        neo_pixels.next(7, 7)
    except MemoryError as e:
        print(e)
        pass

    time.sleep(0.10)

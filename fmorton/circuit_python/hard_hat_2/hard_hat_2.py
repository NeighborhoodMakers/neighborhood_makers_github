import gc
import time
import board
import neopixel
import makers_remote_control

def move_cursor(neo_pixels_cursor, movement):
    neo_pixels_cursor += movement
    if neo_pixels_cursor < 4:
        return(4)
    elif neo_pixels_cursor > 39:
        return(39)
    return(neo_pixels_cursor)

NOTHING = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)

remote_control = makers_remote_control.RemoteControl(debug=False)

neo_pixels = neopixel.NeoPixel(board.A1, 43, brightness=0.02, auto_write=False)
neo_pixels_cursor = 21

neo_pixels.fill(PURPLE)
neo_pixels.show()

while True:
    code = remote_control.code(blocking=True)

    if code == remote_control.LEFT:
        neo_pixels_cursor = move_cursor(neo_pixels_cursor, -2)
    elif code == remote_control.RIGHT:
        neo_pixels_cursor = move_cursor(neo_pixels_cursor, 2)

    if code != -1:
        print("DEBUG: code is ", code, " free memory is ", gc.mem_free(), " cursor is ", neo_pixels_cursor)

    neo_pixels.fill(BLUE)
    for i in range(neo_pixels_cursor - 2, neo_pixels_cursor + 2):
        neo_pixels[i] = WHITE

    neo_pixels.show()
    #neo_pixels.fill(CYAN)
    #neo_pixels[22] = GREEN
    #neo_pixels.show()

    if code == remote_control.UNKNOWN:
        print("sleeping...")
        time.sleep(0.1)

    gc.collect()



"""
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
#neo_pixels = hard_hat_neo_pixels.HardHatNeoPixels(43)

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
"""

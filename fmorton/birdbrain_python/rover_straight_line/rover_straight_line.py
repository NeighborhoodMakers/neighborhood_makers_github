from BirdBrain import Hummingbird
import time

def forward(rover, speed):
    #rover.setRotationServo(1, speed)
    #rover.setRotationServo(2, -speed)
    pass

def stop():
    pass

rover = Hummingbird('A')

rover.setTriLED(1, 50, 50, 75)
rover.setTriLED(2, 50, 50, 75)

#while True:
    #if keyboard.is_pressed('left'):
        #print("left")
#    pass

forward(rover, 50)

time.sleep(1)

rover.stopAll()

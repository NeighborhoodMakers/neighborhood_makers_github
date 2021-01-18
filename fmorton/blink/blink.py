from BirdBrain import Hummingbird, Microbit
import time

myBird    = Hummingbird('A')

for i in range(0,10):
        print("on")
        myBird.setLED(1,100)
        time.sleep(.25)
        print("off")
        myBird.setLED(1,0)
        time.sleep(.25)
		
myBird.stopAll()

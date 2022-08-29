from BirdBrain import Hummingbird
import time

myBird = Hummingbird('A')

for i in range(0,10):
        print("on")
        myBird.setTriLED(1,50,50,50)
        time.sleep(.25)
        print("off")
        myBird.setTriLED(1,0,0,0)
        time.sleep(.25)
		
myBird.stopAll()
# Write your code here :-)

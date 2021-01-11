from BirdBrain import Hummingbird, Microbit
import sys
import time

myBird    = Hummingbird('A')

print(sys.path)

for i in range(0,10):
	myBird.setLED(1,100)
	time.sleep(1)
	myBird.setLED(1,0)
	time.sleep(1)
		
myBird.stopAll()

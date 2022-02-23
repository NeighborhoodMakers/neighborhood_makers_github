# Write your code here :-)
from BirdBrain import Finch
import time

finch = Finch()

finch.setPoint(1,1,1)
finch.setPoint(1,5,1)
finch.setPoint(5,1,1)
finch.setPoint(5,5,1)

time.sleep(2)

finch.setPoint(1,1,0)
finch.setPoint(1,5,0)
finch.setPoint(5,1,0)
finch.setPoint(5,5,0)

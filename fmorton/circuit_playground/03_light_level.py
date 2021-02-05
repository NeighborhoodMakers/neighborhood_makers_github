import time
 
import analogio
import board
 
#light = analogio.AnalogIn(board.LIGHT)
light = analogio.AnalogIn(board.MICROPHONE_DATA)
#light = analogio.AnalogIn(board.MICROPHONE_CLOCK)

while True:
    print((light.value,))
    #time.sleep(0.1)
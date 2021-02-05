import board
import digitalio
import time

connection_1 = digitalio.DigitalInOut(board.A3)
connection_1.direction = digitalio.Direction.INPUT
connection_1.pull = digitalio.Pull.DOWN

while True:
  connection_1_connected = connection_1.value

  print(connection_1_connected)

  time.sleep(0.25)


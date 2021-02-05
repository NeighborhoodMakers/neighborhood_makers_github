import time
import pulseio
import board
import adafruit_irremote

pulsein = pulseio.PulseIn(board.REMOTEIN, maxlen=120, idle_state=True)
decoder = adafruit_irremote.GenericDecode()

while True:
    pulses = decoder.read_pulses(pulsein, blocking=False)

    if pulses is None:
        print("No pulses")
    else:
        print("Pulses are ", pulses)

    time.sleep(0.1)
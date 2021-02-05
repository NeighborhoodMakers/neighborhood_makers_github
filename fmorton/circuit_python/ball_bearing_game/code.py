import audioio
import board
import time
from adafruit_circuitplayground.express import cpx
from adafruit_crickit import crickit
from random import randint

#import adafruit_irremote
#import pulseio

ss = crickit.seesaw

#pulsein = pulseio.PulseIn(board.REMOTEIN, maxlen=120, idle_state=True)
#decoder = adafruit_irremote.GenericDecode()
#received_code = bytearray(4)

while True:
    print("DEBUG: GET THE PULSES")
    #pulses = decoder.read_pulses(pulsein)
    #print("Heard", len(pulses), "Pulses:", pulses)
    print("click")


#decoder = adafruit_irremote.GenericDecode()

"""
BUTTON_8 = crickit.SIGNAL8

ss.pin_mode(BUTTON_8, ss.INPUT_PULLUP)

#wavfile = "circus.wav"
#wavfile = "rimshot.wav"
#f = open(wavfile, "rb")
#wav = audioio.WaveFile(f)
#a = audioio.AudioOut(board.A0)

while True:
  button_8_connected = ss.digital_read(BUTTON_8)

  if not button_8_connected:
    cpx.pixels.brightness = 0.30
    #cpx.pixels.fill((randint(0, 255), randint(0, 255), randint(0, 255)))
    cpx.pixels.fill((0, 10, 0))


    #a.play(wav)


    

# You can now do all sorts of stuff here while the audio plays
# such as move servos, motors, read sensors...

# Or wait for the audio to finish playing:
    #while a.playing:
      #pass
    
    #f.close()






  else:
    cpx.pixels.brightness = 0.30
    cpx.pixels.fill((10, 0, 0))

  time.sleep(0.25)
"""
import audioio
import pulseio
import board
import time
import mini_remote_control
#from adafruit_circuitplayground.express import cpx
#from adafruit_crickit import crickit
#from random import randint

"""
 Adafruit Mini Remote Control IR Mapping and Mask
 1: [255, 2, 247, 8]             63240
 2: [255, 2, 119, 136]           30600
 3: [255, 2, 183, 72]            46920
 4: [255, 2, 215, 40]            55080
 5: [255, 2, 87, 168]            22440
 6: [255, 2, 151, 104]           38760
 7: [255, 2, 231, 24]            59160
 8: [255, 2, 103, 152]           26520
 9: [255, 2, 167, 88]            42840
 0: [255, 2, 207, 48]            53040
 ^ : [255, 2, 95, 160]           24480
 v : [255, 2, 79, 176]           20400
 > : [255, 2, 175, 80]           44880
 < : [255, 2, 239, 16]           61200
 Enter: [255, 2, 111, 144]       28560
 Setup: [255, 2, 223, 32]        57120
 Stop/Mode: [255, 2, 159, 96]    40800
 Back: [255, 2, 143, 112]        36720
 Vol - : [255, 2, 255, 0]        65280
 Vol + : [255, 2, 191, 64]       48960
 Play/Pause: [255, 2, 127, 128]  32640
"""

class mini_remote_control:
  CODE_UP=128
  CODE_DOWN=129
  CODE_RIGHT=130
  CODE_LEFT=131
  CODE_ENTER=132
  CODE_SETUP=133
  CODE_STOP_MODE=134
  CODE_BACK=135
  CODE_VOL_MINUS=136
  CODE_VOL_PLUS=137
  CODE_PLAY_PAUSE=138
  CODE_UNKNOWN=-1

  def __init__(self, debug=False):
    self.pulsein = pulseio.PulseIn(board.REMOTEIN, maxlen=120, idle_state=True)
    self.decoder = adafruit_irremote.GenericDecode()
    self.debug = debug


  def debug_display(self, *message):
    print("mini_remote_control:", *message)


  def code(self, blocking=False):
    try:
      pulses = self.decoder.read_pulses(self.pulsein, blocking=blocking)

      if(pulses == None): return(self.CODE_UNKNOWN)

      if self.debug: self.debug_display(len(pulses), "pulses:", pulses)

      code = self.decoder.decode_bits(pulses, debug=False)

      if self.debug: self.debug_display("decoded:", code)

      if((code[0] != 255) or (code[1] != 2)): return(self.CODE_UNKNOWN)

      code_mask = (code[2] << 8) | code[3]

      if(code_mask == 53040): return(0)
      if(code_mask == 63240): return(1)
      if(code_mask == 30600): return(2)
      if(code_mask == 46920): return(3)
      if(code_mask == 55080): return(4)
      if(code_mask == 22440): return(5)
      if(code_mask == 38760): return(6)
      if(code_mask == 59160): return(7)
      if(code_mask == 26520): return(8)
      if(code_mask == 42840): return(9)
      if(code_mask == 24480): return(self.CODE_UP)
      if(code_mask == 20400): return(self.CODE_DOWN)
      if(code_mask == 44880): return(self.CODE_RIGHT)
      if(code_mask == 61200): return(self.CODE_LEFT)
      if(code_mask == 28560): return(self.CODE_ENTER)
      if(code_mask == 57120): return(self.CODE_SETUP)
      if(code_mask == 40800): return(self.CODE_STOP_MODE)
      if(code_mask == 36720): return(self.CODE_BACK)
      if(code_mask == 65280): return(self.CODE_VOL_MINUS)
      if(code_mask == 48960): return(self.CODE_VOL_PLUS)
      if(code_mask == 32640): return(self.CODE_PLAY_PAUSE)

      return(self.CODE_UNKNOWN)
    except adafruit_irremote.IRNECRepeatException:
      if self.debug: self.debug_display("repeat exception")
      return(self.CODE_UNKNOWN)
    except adafruit_irremote.IRDecodeException as e:
      if self.debug: self.debug_display("failed to decode:", e.args)
      return(self.CODE_UNKNOWN)
    except MemoryError as e:
      if self.debug: self.debug_display("memory error:", e.args)
      return(self.CODE_UNKNOWN)



#ss = crickit.seesaw



mini_remote = mini_remote_control(debug=False)

while True:
    code = mini_remote.code()

    if(code != 0): print("mini_remote_control code:", code)

    time.sleep(0.25)
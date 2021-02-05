import time
import board
import neopixel

class HardHatNeoPixels:
    RED = (255, 0, 0)
    YELLOW = (255, 150, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLUE = (0, 0, 255)
    PURPLE = (180, 0, 255)
    WHITE = (128, 128, 128) 
    NOTHING = (0, 0, 0) 

    def __init__(self, num_pixels):
        self.num_pixels = num_pixels
        self.neo_pixels = neopixel.NeoPixel(board.A1, 
            self.num_pixels, brightness=0.3,
            auto_write=False)
        self.idle_pixel = 0

    def idle(self, color):
        print("DEBUG: set pixel", self.idle_pixel)
        self.neo_pixels[self.idle_pixel] = color
        self.neo_pixels.show()
        self.idle_pixel += 1
        if self.idle_pixel >= self.num_pixels:
            self.idle_pixel = 0
            self.clear()
        #for pixel in range(self.num_pixels):
        #    self.neo_pixels[pixel] = self.WHITE
        #    self.neo_pixels.show()
        #    time.sleep(0.005)

    def fill(self, color):
        self.neo_pixels.fill(color)
        self.neo_pixels.show()

    def clear(self):
        self.fill(self.NOTHING)
import board
import neopixel
from random import randint

class HardHatAnimatedNeoPixels:
    RED = (255, 0, 0)
    YELLOW = (255, 150, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLUE = (0, 0, 255)
    PURPLE = (180, 0, 255)
    WHITE = (128, 128, 128) 
    NOTHING = (0, 0, 0) 

    def __init__(self, num_pixels, color=NOTHING, width=4):
        self.num_pixels = num_pixels
        self.current_color = color
        self.width = width

        self.neo_pixels = neopixel.NeoPixel(board.A1, 
            self.num_pixels, brightness=0.3,
            auto_write=False)
        self.current_pixel = 0
        self.next_scan_pixel = 0
        self.next_scan_pixel_color = self.NOTHING


    def color(self, color):
        self.current_color = color

    def next(self, width=1, offset=0):
        for index in (range(0, width)):
            pixel = self.current_pixel+(index*offset)
            if pixel < self.num_pixels:
                #print("pixel",self.current_pixel,index,offset,pixel)
                self.neo_pixels[pixel] = self.current_color
        self.neo_pixels.show()
        self.current_pixel += width
        if self.current_pixel >= self.num_pixels:
            self.current_pixel = randint(0, int(self.num_pixels / 3))
            #self.clear()
        #for pixel in range(self.num_pixels):
        #    self.neo_pixels[pixel] = self.WHITE
        #    self.neo_pixels.show()
        #    time.sleep(0.005)

    def shift(self, amount=1):
        for index in range(amount, self.num_pixels-amount):
            self.neo_pixels[index] = self.neo_pixels[index+amount]
        self.neo_pixels.show()

    def scan(self, color):
        for index in (range(0, self.num_pixels)):
            previous_color = self.neo_pixels[index]
            self.neo_pixels[index] = color
            self.neo_pixels.show()
            self.neo_pixels[index] = previous_color
            #self.neo_pixels.show()

    def fill(self, color):
        self.neo_pixels.fill(color)
        self.neo_pixels.show()

    def clear(self):
        self.fill(self.NOTHING)

    def random_color(self, min=0, max_red=255, max_green=255, max_blue=255):
        red = randint(min, randint(min, max_red))
        green = randint(min, randint(min, max_green))
        blue = randint(min, randint(min, max_blue))

        return((red, green, blue))
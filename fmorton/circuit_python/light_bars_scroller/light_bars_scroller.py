import time
import board
import neopixel
from random import randint

neo_pixel_count = 8

red_range = [ 0, 255 ]
green_range = [ 0, 255 ]
blue_range = [ 0, 255 ]

neo_pixels = neopixel.NeoPixel(board.A1, neo_pixel_count)

while True:
    red = randint(red_range[0], red_range[1])
    green = randint(green_range[0], green_range[1])
    blue = randint(blue_range[0], blue_range[1])

    for pixel in range(0, neo_pixel_count - 1):
        neo_pixels[pixel] = neo_pixels[pixel + 1]

    neo_pixels[7] = (red, green, blue)

    neo_pixels.show()

    time.sleep(0.051)
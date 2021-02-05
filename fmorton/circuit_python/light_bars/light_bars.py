import time
import board
import neopixel
from random import randint,uniform
import random

neo_pixel_count = 8

red_range = [ 0, 255 ]
green_range = [ 0, 255 ]
blue_range = [ 0, 255 ]

shortest_sleep = 0.0
longest_sleep = 0.25

neo_pixels = neopixel.NeoPixel(board.A1, neo_pixel_count)

while True:
    for pixel in range(0, neo_pixel_count):
        red = randint(red_range[0], red_range[1])
        green = randint(green_range[0], green_range[1])
        blue = randint(blue_range[0], blue_range[1])

        neo_pixels[pixel] = (red, green, blue)
        neo_pixels.show()

    time.sleep(random.uniform(shortest_sleep, longest_sleep))
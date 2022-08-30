import time
import random
import board
import neopixel

PIXEL_COUNT = 60
NOTHING = (0, 0, 0)
WHITE = (180, 180, 180)
RED = (180, 0, 0)
BLUE = (0, 0, 180)
PURPLE = (180, 0, 255)

def random_color(colors):
    #return(colors[random.randint(0, len(colors) - 1)])
    return(random.choice(colors))

def random_fill(neo_pixels, colors):
    for pixel in range(0, PIXEL_COUNT - 1):
        neo_pixels[pixel] = random_color(colors)

        neo_pixels.show()

def progressive_fill(neo_pixels, colors):
    for pixel in range(0, PIXEL_COUNT - 1):
        neo_pixels[pixel] = random_color(colors)
        neo_pixels.show()
        time.sleep(0.015)


neo_pixels = neopixel.NeoPixel(board.A1, PIXEL_COUNT, brightness=1.02, auto_write=False)

neo_pixels.fill(NOTHING)
neo_pixels.show()

while True:
    mode = random.randint(0, 100)

    if mode < 75:
        neo_pixels.fill(NOTHING)
        neo_pixels.show()
    elif mode < 92:
        random_fill(neo_pixels, [ WHITE, WHITE, NOTHING ])
    elif mode < 97:
        random_fill(neo_pixels, [ WHITE, PURPLE, NOTHING ])
    else:
        progressive_fill(neo_pixels, [ WHITE, WHITE, PURPLE, BLUE, RED, RED ])

    time.sleep(random.random() / 4.0)


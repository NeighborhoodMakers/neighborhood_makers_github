import time
import board
import neopixel

neo_pixel_count = 8

neo_pixels = neopixel.NeoPixel(board.A1, neo_pixel_count)

active_pixel = 0
active_pixel_color = (255, 0, 0)

while True:
    neo_pixels.fill((0, 0, 0))

    pixel = (active_pixel % (neo_pixel_count * 2))

    if pixel >= neo_pixel_count:
        pixel = neo_pixel_count - (pixel - neo_pixel_count) - 1

    neo_pixels[pixel] = active_pixel_color
    neo_pixels.show()

    active_pixel += 1

    time.sleep(0.02)
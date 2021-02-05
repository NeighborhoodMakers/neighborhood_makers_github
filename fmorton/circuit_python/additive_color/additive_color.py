import board
import neopixel

neo_pixels = neopixel.NeoPixel(board.A1, 8)

neo_pixels[0] = (0, 0, 0)
neo_pixels[1] = (255, 0, 0)
neo_pixels[2] = (0, 255, 0)
neo_pixels[3] = (0, 0, 255)
neo_pixels[4] = (255, 255, 0)
neo_pixels[5] = (255, 0, 255)
neo_pixels[6] = (0, 255, 255)
neo_pixels[7] = (255, 255, 255)

neo_pixels.show()
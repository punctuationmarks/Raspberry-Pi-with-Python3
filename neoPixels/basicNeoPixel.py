import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 30)

# "fills" all of the neopixels with the same color light
pixels.fill((0, 255, 0))
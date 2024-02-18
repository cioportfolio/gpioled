import board
import neopixel
import colorsys
import time

def rainbow(hue):
    r,g,b = colorsys.hsv_to_rgb(hue%100/100,1.0,1.0)
    return (int(255*r),int(255*g),int(255*b))

strip=neopixel.NeoPixel(board.D21, 32, brightness=0.2)

h=0

for _ in range(200):
    strip.fill(rainbow(h))
    strip.show()
    time.sleep(.1)
    h+=1
strip.fill((0,0,0))
strip.show()
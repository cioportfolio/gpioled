# gpioled
Driving LEDS using RPi GPIOs. Based on [these instructions](https://learn.adafruit.com/neopixels-on-raspberry-pi/raspberry-pi-wiring).

## Libraries

```
> sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
> sudo python3 -m pip install --force-reinstall adafruit-blinka
```

If loading from libraries previously saved with pip3 download add `--find-links <path> --no-index` options

## Running

Access to GPIO pins requires admin rights so use `sudo python3 ...` or `sudo Thonny`

## Pins

The library uses hardware support to handle the precise timing needed by the LEDs but this is only available on pins 10,12,18 and 21. Some of these pins have other functions that can get in the way (e.g. Pin 18 can't be used unless the sound is disabled). Pin 21 seems to work without any further setting changes.

## Power

The 5v supply on the raspberry pi is limited. For large numbers of LEDs external power will be needed to maintain the full range of colours. At 20% power (as used in the demo python programme) ws2812b LEDs are still quite bright and a raspberry pi can comfortably power around 250 LEDs (e.g. an 8 x 32 matrix)

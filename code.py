import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = False

time.sleep(10)

while True:
    led.value = True

    keyboard.press(Keycode.WINDOWS, Keycode.R)
    keyboard.release(Keycode.WINDOWS, Keycode.R)

    time.sleep(0.1)

    keyboard.send(Keycode.C)
    keyboard.send(Keycode.M)
    keyboard.send(Keycode.D)
    
    keyboard.press(Keycode.LEFT_CONTROL, Keycode.T)
    keyboard.release(Keycode.LEFT_CONTROL, Keycode.T)

    keyboard.send(Keycode.ENTER)
    keyboard.send(Keycode.ENTER)

    led.value = False

    time.sleep(0.3)

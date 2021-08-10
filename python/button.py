from microbit import *

while True:
    #LED1
    i2c.write(0x20, b'\1', repeat=True)
    sleep(1000)
    i2c.write(0x20, b'\0', repeat=True)
    sleep(1000)
    #LED2
    i2c.write(0x20, b'\2', repeat=True)
    sleep(1000)
    i2c.write(0x20, b'\0', repeat=True)
    sleep(1000)
    #LED3
    i2c.write(0x20, b'\4', repeat=True)
    sleep(1000)
    i2c.write(0x20, b'\0', repeat=True)
    sleep(1000)
    #LED4
    i2c.write(0x20, b'\8', repeat=True)
    sleep(1000)
    i2c.write(0x20, b'\0', repeat=True)
    sleep(1000)
    #ALL LEDS
    i2c.write(0x20, b'xf', repeat=True)
    sleep(1000)
    i2c.write(0x20, b'\0', repeat=True)
    sleep(1000)

import smbus
import time

bus = smbus.SMBus(1)

while True:
	bus.write_byte(0x20, 0xFFFF)
	time.sleep(0.5)
	bus.write_byte(0x20, 0x00FF)
	time.sleep(0.5)
	bus.write_byte(0x20, 0x0000)
	time.sleep(0.5)

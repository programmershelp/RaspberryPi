import smbus
import time
 
#bus = smbus.SMBus(0)  #Pi 1 uses 0
bus = smbus.SMBus(1) #Pi 2 uses 1
 
DEVICE = 0x20 # Device address (A0-A2)
IODIRA = 0x00
OLATA  = 0x14
GPIOA  = 0x12
 
# Set all GPA pins as outputs
bus.write_byte_data(DEVICE,IODIRA,0x00)
 
# Set output all 7 output bits to 0
bus.write_byte_data(DEVICE,OLATA,0)
 
for LedOut in range(1,255):
  # Count from 1 to 255
  bus.write_byte_data(DEVICE,OLATA,LedOut)
  print LedOut
  time.sleep(0.1)
 
# Set all bits to zero
bus.write_byte_data(DEVICE,OLATA,0)
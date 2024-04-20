import RPi.GPIO as gpio
import time

time.sleep(0.5)
print("leds turn on...")
time.sleep(0.2)
print("leds turn off...")
time.sleep(0.3)
print("a project")
time.sleep(0.1)
print("by Ferret")
time.sleep(0.5)
print(" ")
print("="*20)
print("       LEDS")
print("="*20)
print(" ")
time.sleep(0.2)


gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.OUT) # red led
gpio.output(12, 0) # off
gpio.setup(29, gpio.OUT) # yellow led
gpio.output(29, 0) # off
gpio.setup(31, gpio.OUT) # green led
gpio.output(31, 0) # off
gpio.setup(33, gpio.OUT) # blue led
gpio.output(33, 0) # off

for i in range(5):
	time.sleep(0.5)
	gpio.output(33, 0)
	gpio.output(12, 1)
	time.sleep(0.5)
	gpio.output(12, 0)
	gpio.output(29, 1)
	time.sleep(0.5)
	gpio.output(29, 0)
	gpio.output(31, 1)
	time.sleep(0.5)
	gpio.output(31, 0)
	gpio.output(33, 1)

time.sleep(0.5)
gpio.cleanup()

print("github.com/ferretosan/rpi-leds")

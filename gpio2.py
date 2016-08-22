# python 2
# vilros t-cobbler
# pin 39 coincides with e20
# resistor b20 (gnd) to b28
# led cathode e28
# led anode e27
# male-to-male d26 to h20 (pin 40 = gpio 21)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 21
GPIO.setup(led, GPIO.OUT)
# switch on
GPIO.output(led, 1)
time.sleep(3)
# switch off
GPIO.output(led, 0)

print "Done"

GPIO.cleanup()

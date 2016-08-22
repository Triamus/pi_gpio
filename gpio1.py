# python 2
# gpio 4 to 9g
# gnd (3rd outer pin) to 4j
# led cathode 8j, anode in 9j

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

GPIO.output(7, True)
time.sleep(3)
GPIO.output(7, False)
time.sleep(3)
GPIO.output(7, True)
time.sleep(3)
GPIO.output(7, False)

print "Done"

GPIO.cleanup()

# python 3
# sunfounder t-cobbler
# pin 39 coincides with c20
# resistor j17 (gnd) to j21
# led cathode i21
# led anode i20
# male-to-male a18 (gpio19) to a30
# male-to-male a20 (gnd) to a28
# button d28, d30, g28, g30
# how to exit?

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
 
# Pin 19 will sense for button pushing
button = 19
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
# The LED
led = 21
GPIO.setup(led, GPIO.OUT)
 
while True:
    input_state = GPIO.input(button) # Sense the button
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
        # Switch on LED
        GPIO.output(led, 1)
    else :
        # Switch off LED
        GPIO.output(led, 0)
        
GPIO.cleanup()

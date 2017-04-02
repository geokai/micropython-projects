# This script pulses the on-board led at varying speeds depending on
# parameters:

# This script presented by Damien George at the GOTO 2016 conference.

# This file was created on 18/03/17
# Author: George Kaimakis
# Modifyed with an infinite loop and an extra delay at the low point
# in order to smeeth out the pulsing


import machine, time

extra_delay = 140


# create a pwm object on pin 2:
pwm2 = machine.PWM(machine.Pin(2))

def pulse(p, d):
    while True:
        # pwm is 10 bit 0-1023. pin is active low:
        for i in range(1020, -1, -50):
            p.duty(i)
            time.sleep_ms(d)
        for i in range(0, 1020, 3):
            p.duty(i)
            time.sleep_ms(d)
        time.sleep_ms(extra_delay)

pulse(pwm2, 4)

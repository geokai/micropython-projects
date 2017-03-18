# This script pulses the on-board led at varying speeds depending on
# parameters:

# This script presented by Damien George at the GOTO 2016 conference.

# This file was created on 18/03/17
# Author: George Kaimakis
# Modifyed with an infinite loop and an extra delay at the low point
# in order to smeeth out the pulsing


import machine, time

extra_delay = 200

#p16 = machine.Pin(16, machine.Pin.OUT)
p2 = machine.Pin(2, machine.Pin.OUT)
#p2.high()
p2.low()

#pwm16 = machine.PWM(machine.Pin(16))
pwm2 = machine.PWM(machine.Pin(2))

def pulse(p, d):
    while True:
        for i in range(1015, -1, -4):
            p.duty(i)
            time.sleep_ms(d)
        for i in range(0, 1015, 3):
            p.duty(i)
            time.sleep_ms(d)
        time.sleep_ms(extra_delay)

pulse(pwm2, 4)

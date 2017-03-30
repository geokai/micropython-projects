# This script uses the DHT22 sensor to return temperature and humidity.
# Uses a one-wire method of connection to the device:

# This file was created on 30/03/2017
# Author: George Kaimakis


import machine
import dht
from time import sleep

sen = dht.DHT22(machine.Pin(2))

INTERVAL    = 10    # delay between readings:
PAUSE       = 0.5   # small pause before printing results (for effect!):

# print the device id before entering the loop:
print()
print('sensor id {}'.format('dht'))     # not a sensor scan:
print()

counter = 0     # reset counter:

while True:
    print("Checking Temp & Humidity...{0}".format(counter + 1))
    #print()
    sen.measure()
    sleep(PAUSE)
    print("Temperature \t{0:3.1f} Celcius".format(sen.temperature()))
    print()
    print("Humidity \t{0:3.1f} % RH".format(sen.humidity()))
    print()
    counter += 1    # increment counter:
    sleep(INTERVAL)

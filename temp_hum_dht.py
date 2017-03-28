import machine
import dht
from time import sleep

sen = dht.DHT22(machine.Pin(2))

print()
print('sensor id {}'.format('dht'))
print()
counter = 0
while True:
    print("Checking Temp & Humidity...{0}".format(counter + 1))
    #print()
    sen.measure()
    sleep(0.5)
    print("Temperature \t{0:3.1f} Celcius".format(sen.temperature()))
    print()
    print("Humidity \t{0:3.1f} % RH".format(sen.humidity()))
    print()
    counter += 1
    sleep(600)

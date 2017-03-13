import machine
import dht
from time import sleep

sen = dht.DHT22(machine.Pin(2))

counter = 0
while True:
    print("Checking Temp & Humidity...{0}".format(counter + 1))
    #print()
    sen.measure()
    sleep(2)
    print("Temp \t{0:3.1f}C".format(sen.temperature()))
    print("Hum \t{0:3.1f}%".format(sen.humidity()))
    print()
    counter += 1
    sleep(300)

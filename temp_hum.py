import machine
import dht
from time import sleep

sen = dht.DHT22(machine.Pin(2))

while True:
    print("Checking Temp & Humidity...")
    sleep(2)
    print()
    sen.measure()
    print('Temp {0}C'.format(sen.temperature()))
    print('Hum {0}%'.format(sen.humidity()))
    print()
    sleep(180)

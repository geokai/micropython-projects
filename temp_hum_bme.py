import machine
import bme280
from time import sleep

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
bme = bme280.BME280(i2c=i2c)

print()
print('sensor id {0}'.format(i2c.scan()))
print()
counter = 0
while True:
    print("Checking Temp, Pressure & Humidity ...{0}".format(counter + 1))
    #print()
    reading = bme.values
    sleep(0.5)
    print("Temperature \t{0:s}elcius".format(bme.values[0]))
    print("Pressure \t{0:s}scal".format(bme.values[1]))
    print("Humidity \t{0:s} RH".format(bme.values[2]))
    print()
    counter += 1
    sleep(600)

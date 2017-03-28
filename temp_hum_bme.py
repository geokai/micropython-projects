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
    readings = bme.read_compensated_data()
    sleep(0.5)
    print("Temperature  \t{0:6.1f} Celcius".format(readings[0]/100))
    print("Pressure \t{0:6.1f} hPa".format(readings[1]/256/100))
    print("Humidity \t{0:6.1f} % RH".format(readings[2]/1024))
    print()
    counter += 1
    sleep(600)

import machine
from time import sleep_ms

led = machine.Pin(2, machine.Pin.OUT)
led.low()

print("Hello World!")
for i in range(1, 11):
    print(i)

while True:
    print('Flash!')
    sleep_ms(1000)

"""simple led flash script as a verification the board is operational"""

from time import sleep_ms
import machine

led = machine.Pin(2, machine.Pin.OUT)

for x in range(4):
    led.value(0)
    sleep_ms(500)
    led.value(1)
    sleep_ms(500)

print()
print("Hello World!")
for i in range(1, 11):
    sleep_ms(250)
    print(i)
print()
sleep_ms(250)

while True:
    print('Flash!')
    led.value(0)
    sleep_ms(250)
    led.value(1)
    sleep_ms(250)

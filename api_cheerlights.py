# and parse out the latest 'color' information using the 'ujson' method. 
# This micropython script will make a request to the cheerlights api

import urequests
import time
import neopixel
import machine


# Global variables:
RECVD_COLOR         = ''
PREVIOUS_COLOR      = ''
PIXEL_PIN           = 0
NEW_COLOR           = ''

INTERVAL            = 20000

host                = 'https://thingspeak.com/'
topic               = 'channels/1417/feeds/last.json'
api                 = host + topic


colors = {'red':(255,0,0), 'orange':(255,165,0), 'yellow':(255,255,0),
'green':(0,128,0), 'cyan':(0,255,255), 'blue':(0,0,255), 'purple':(128,0,128),
'magenta':(255,0,255), 'pink':(255,192,203), 'white':(255,255,255),
'oldlace':(253,245,230), 'warmwhite':(253,245,230)}

def api_request(url):
    global RECVD_COLOR
    feed = urequests.get(url)
    color = feed.json()['field1']
    RECVD_COLOR = color
    return None

def recvd_color_test(color):
    global NEW_COLOR
    if color in colors:
        NEW_COLOR = colors[color]
    return None

def new_neopixel_color(next_color):
    np.fill(next_color)
    np.write()
    return None

# define pin and create neopixel object:
pin = machine.Pin(PIXEL_PIN)
np = neopixel.NeoPixel(pin, 1)

count = 0
while True:
    api_request(api)
    if RECVD_COLOR == PREVIOUS_COLOR:
        count += 1
        print(str(count) + ': ' + RECVD_COLOR)
    else:
        count = 1
        print(str(count) + ': ' + RECVD_COLOR)
        recvd_color_test(RECVD_COLOR)
        new_neopixel_color(NEW_COLOR)
        PREVIOUS_COLOR = RECVD_COLOR
    time.sleep_ms(INTERVAL)

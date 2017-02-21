import esp
esp.osdebug(None)
import gc

def do_connect(ssid, password):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('network config: ', sta_if.ifconfig())

do_connect(ssid, password)  # replace args with credentials:

import webrepl
webrepl.start()
gc.collect()

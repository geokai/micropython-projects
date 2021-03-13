#!/usr/local/bin/python3


import requests
import time
from datetime import datetime
import os


def cheerlight():
    os.system('clear')
    api = 'https://thingspeak.com/channels/1417/feeds/last.json'
    def api_request(url):
       feed = requests.get(url)
       return feed.json()['field1']

    while True:
        color = api_request(api)
        ts = time.time_ns()//1000000000
        recv_time = datetime.fromtimestamp(ts)
        print("{}, ".format(recv_time), end="")
        print("cheerlights color: {}".format(color))
        time.sleep(20)


cheerlight()

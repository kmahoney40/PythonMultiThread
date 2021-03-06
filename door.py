import time
import piplates.RELAYplate as RELAY
import relay_plate
import requests
import datetime


class Door:
    def __init__(self, pid, cfgObj):
        self.name = "Door"
        self.url = cfgObj.url + "door"
        self.pid = pid
    def door_cmnd(self, override):
        now = datetime.datetime.now()
        ret_json = str(now) + str(requests.get(self.url).text)

        if str(ret_json).find('true') > -1 or override == True:
            RELAY.relayON(self.pid, 5)
            time.sleep(0.5)
            RELAY.relayOFF(self.pid, 5)
        else:
            RELAY.relayOFF(self.pid, 5)
        return ret_json


import time
import piplates.RELAYplate as RELAY
import requests


class Door:
    def __init__(self, cfgObj):
        self.name = "Door"
        self.url = cfgObj.url + "door"

    def door_cmnd(self, override):
        door_json = str(requests.get(self.url).text)

        if str(door_json.text).find('true') > -1 or override == True:
            RELAY.relayON(0, 5)
            time.sleep(0.5)
            RELAY.relayOFF(0, 5)
        else:
            RELAY.relayOFF(0, 5)
        return door_json


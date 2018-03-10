#import piplates.DAQCplate as DAQC
import sys
import requests
import json
import daqc_plate
import relay_plate

class PiPlates:
    def __init__(self, cfgObj):
        self.name = "PiPlates"
        self.count = 0
        self.url = cfgObj.url + 'piplates'
        self.headers = {'content-type': 'application/json'}
        ret_str = ''
    #__init__

    def read_write_io(self, cfgObj, ret):
        method_name = "read_write_io"
        try:
            daqc = daqc_plate.DaqcPlate(0, cfgObj)
            ret[0] = daqc.read_adc()

            # time: 1520710505.0
            # t1: 19.2
            # t2: 16.8
            # t3: 16.0
            # v: 3.764

            #relay = relay_plate.RelayPlate(0, ret[0], cfgObj)
            relay = relay_plate.RelayPlate(0, cfgObj, ret[0])
            ret[1] = relay.set_relays()

            ret[2][0] = self.write_to_server(ret)
        except Exception, ex:
            sys.exit("Error in " + self.name + "." + method_name)
    #read_write_io

    def write_to_server(self, ret):
        daqc = ret[0]
        relay = ret[1]
#        payload = {"TEMP_1": daqc.get('t1'), "TEMP_2": daqc.get('t2'), "TEMP_3": daqc.get('t3'), "VOLTAGE": daqc.get('v'), "FAN_ON": relay.get('r7'), "CHARGER_ON": relay.get('r3')};
        
#        r = requests.post(self.url, json=json.dumps(payload), headers=self.headers)
        return "asdfasd"#str(r.status_code) + ": " + r.text#requests.post(self.url, json=json.dumps(payload), headers=self.headers)
    #create_return
#PiPlates

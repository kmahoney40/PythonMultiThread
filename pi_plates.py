#import piplates.DAQCplate as DAQC
import daqc_plate
import relay_plate
import sys

class PiPlates:
    def __init__(self, cfgObj, ret):
        self.name = "PiPlates"
        self.count = 0
        #self.cfgObj = cfgObj
        #self.
    #__init__

    def read_write_io(self, cfgObj, ret):
        method_name = "read_write_io"
        try:
            daqc = daqc_plate.DaqcPlate(0, cfgObj)
            ret[0] = daqc.read_adc()
            
            #relay = relay_plate.RelayPlate(0, ret[0], cfgObj)
            relay = relay_plate.RelayPlate(0, cfgObj, ret[0])
            ret[1] = relay.set_relays()
        except Exception, ex:
            sys.exit("Error in " + self.name + "." + method_name)
    #read_write_io

#PiPlates

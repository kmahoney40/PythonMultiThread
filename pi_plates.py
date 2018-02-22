#import piplates.DAQCplate as DAQC
import piplates.RELAYplate as RELAY
import daqc_plate
import relpay_plate
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
            ret = daqc.read_adc()
            ret[0] = daqc.read_adc()
            
            #realy = relay_plate.RealyPalte(0, daqc, cfgObj)
            #ret[1][0] = 7# relay.set_realys()
        except Exception, ex:
            sys.exit("Error in " + self.name + "." + method_name)
    #read_write_io

    def initial_state():
        set_relay(0, 3, 0)
        set_relay(0, 5, 0)
        set_realy(0, 7, 0)
    #initial_state

    #def set_relays(self)
        
    #set_rleays

    def set_relay(self, rid, idx, state):
        method_name = "set_relay"
        try:
            if state != 0:
                RELAY.relayON(rid, idx)
            else:
                RELAY.relayOFF(rid, idx)
        except Exception, ex:
            sys.exti("Error in " + self.name + "." + method_name + ": " + traceback.format_exc())
    #set_relay
#PiPlates

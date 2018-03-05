import piplates.RELAYplate as RELAY
#import sys

class RelayPlate:
    def __init__(self, pid, cfgObj, daqc_dict):
        try:
            self.name = "RelayPlate"
            self.pid = pid
            self.daqc_dict = daqc_dict
            self.fan_change_temp = cfgObj.fanChangeTemp
            self.fan_delta = cfgObj.fanDelta
            self.bat_voltage = daqc_dict.get('v')#.cfgObj.volts
            self.voltage_trigger = cfgObj.voltageTrigger
            self.fan_on = False
        except Exception, ex:
            sys.exit("Error in RelayPlate: " + str(ex))

    def reset_relays(self):
        for idx in list(range(7)):
            RELAY.relayOFF(self.pid, idx)

    def set_relay(self, rid, state):
        if state != 0:
            RELAY.relayON(self.pid, rid)
        else:
            RELAY.relayOFF(self.pid, rid)

    def get_bool(self, state, exp):
        ret_val = False
        if state & (2 ** exp) > 0:
            ret_val = True
        return ret_val

    def get_state_dict(self):
#        return {'r1': True}
        ret_dict = {}
        state = RELAY.relaySTATE(self.pid)
        for idx in list(range(7)):
            key = 'r' + str(idx+1)
            ret_dict[key] = self.get_bool(state, idx)
        return ret_dict

    def set_relays(self):
        if self.bat_voltage < self.voltage_trigger:
            self.set_relay(7, 1)
        else:
            self.set_relay(7, 0)

        if self.daqc_dict.get('t1') > self.fan_change_temp + self.fan_delta:
            self.set_relay(3, 1)
            self.fan_on = True
#            self.fanChanged = True
        elif self.daqc_dict.get('t1') < self.fan_change_temp - self.fan_delta:
            self.set_relay(3, 0)
            self.fan_on = False
#            self.fanChanged = True

        return  self.get_state_dict()# {'r1': True}#self.getate_dict()#_state_dict()

#
#class RelayPlate:
#    def __inti__(self, pid, daqcDict, cfgObj):
#        try:
#            self.name = "RelayPlate"
#        except Exception, ex:
#            sys.exit("Error in " + self.name)
        #self.pid = pid
        #self.daqc = daqc
        #self.volts = daqcDict.get('v')
        #self.t1 = daqcDict.get('t1')
        #self.fanOn = False
        #self.relay_state = [0, 0, 0, 0, 0, 0, 0]
        #self.set_initial_state()
        #self.fanChangeTemp = cfgObj.get('fanChangeTemp')
        #self.fanDelta = cfgObj.get('fanDelta')
    #__init__


#    def set_relay(self, idx, state):
#        method_name = "set_realy"
#        if state != 0:
#            RELAY.relayON(self.pid, idx)
#            self.realy_state[idx] = state
#        else:
#            RELAY.relayOFF(self.pid, idx)
#        self.realy_state[idx] = state
#    #set_relay
#
#    def set_initial_state(self):
#        for idx in list(range(7)):
#            self.set_relay(idx, 0)
#    #initial_state

    def set_relays1(self):
        return {'r1': False}

#        if self.volts < cfgObb.get('voltageTrigger'):
#            self.set_relay(7, 1)
#        else:
#            self.set_relay(7, 0)
#
#        if self.fanOn and self.t1 < self.fanChangeTemp + self.fanDelta:
#            self.set_relay(3, 1)
#            self.fanOn = True
#            self.fanChanged = True
#        else:
#            self.set_relay(3, 0)
#            self.fanOn = False
#            self.fanChanged = True
#
#        return self.relay_state
#    #set_relays
##RelayPlate

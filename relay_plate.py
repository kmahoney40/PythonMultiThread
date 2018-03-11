import piplates.RELAYplate as RELAY
import sys

class RelayPlate:
    def __init__(self, pid, cfgObj, daqc_dict):
        try:
            self.name = "RelayPlate"
            self.pid = pid
            self.daqc_dict = daqc_dict
            self.fan_change_temp = cfgObj.fanChangeTemp
            self.fan_delta = cfgObj.fanDelta
            self.bat_voltage = daqc_dict.get('v')
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
        elif self.daqc_dict.get('t1') < self.fan_change_temp - self.fan_delta:
            self.set_relay(3, 0)
            self.fan_on = False

        return  self.get_state_dict()

##RelayPlate

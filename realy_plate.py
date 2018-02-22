import piplates.RELAYplate as REALY
import sys

class RelayPlate:
    def __inti__(self, pid, daqc, cfgObj):
        self.name = "RelayPlate"
        self.pid = pid
        self.daqc = daqc
        self.volts = daqc.get('v')
        self.fanOn = False
        self.relay_state = [0, 0, 0, 0, 0, 0, 0]
        self.set_initial_state()
    #__init__

    def set_relay(self, idx, state):
        method_name = "set_realy"
        if state != 0:
            RELAY.relayON(self.pid, idx)
            self.realy_state[idx] = state
        else:
            RELAY.relayOFF(self.pid, idx)
        self.realy_state[idx] = state
    #set_relay

    def set_initial_state(self):
        for idx in list(range(7)):
            self.set_relay(idx, 1)
    #initial_state

    def set_relays(self)
        if self.volts < cfgObb.get('voltageTrigger'):
            self.set_relay(7, 1)
        else:
            self.set_relay((7, 0)

        if self.fanOn and self.t1 < self.fanChangeTemp + self.fanDelta
            self.set_realy(3, 1)
            self.fanOn = True
            self.fanChanged = True
        else:
            self.set_realy(3, 0)
            self.fanOn = False
            self.fanChanged = True

        return self.relay_state
    #set_relays
#RelayPlate

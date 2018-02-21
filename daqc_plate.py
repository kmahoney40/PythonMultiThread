import piplates.DAQCplate as DAQC
import sys

class DaqcPlate:
    def __init__(self, pid, cfgObj):
        try:
            self.name = "DaqcPlate"
#           self.pid = pid
        except Exception, ex:
            sys.exit("Error in " + sefl.name)

    def get_adc(idx):
        return DAQC.getADC(self.pid, idx)
    #get_adc

    def get_temp(idx):
        return 100 * get_adc(idx) - 50
    #get_temp

    def read_adc(self):
        t1 = get_temp(0)
        t2 = get_temp(1)
        t2 = get_temp(2)
        v  = get_adc(3)
        return { 't1': t1, 't2': t2, 't3': t3 }
    #read_adc
#DacqPlate

import piplates.DAQCplate as DAQC
import sys

class DaqcPlate:
    def __init__(self, pid, cfgObj):
        try:
            self.name = "DaqcPlate"
            self.pid = pid
        except Exception, ex:
            sys.exit("Error in " + sefl.name)

    def get_adc(self, idx):
        return DAQC.getADC(self.pid, idx)
    #get_adc

    def get_temp(self, idx):
        return 100 * self.get_adc(idx) - 50
    #get_temp

    def read_adc(self):
        #return str(DAQC.getADC(0, 1)) + "      " +  str(self.pid) + str(self.get_adc(1))
        t1 = self.get_temp(0)
        t2 = self.get_temp(1)
        t3 = self.get_temp(2)
        v  = self.get_adc(3)
        return {'t1': t1, 't2': t2, 't3': t3, 'v': v }# str(t1) + " " + str(t2) + " " + str(t3) + " " + str(t3)
    #read_adc
#DacqPlate


# http://code.activestate.com/recipes/496800-event-scheduling-threadingtimer/

import thread
import threading
import readConfig
import readFromServer
import pi_plates
import curses
import piplates.DAQCplate as DAQC
import piplates.RELAYplate as RELAY
import pytz
import requests
import json
import sys
import datetime

class Operation(threading._Timer):
    def __init__(self, *args, **kwargs):
        threading._Timer.__init__(self, *args, **kwargs)
        self.setDaemon(True)
        #self.lastStart = time.time()

    def run(self):
        while True:
            self.finished.clear()
            #self.finished.wait(self.interval - (time.time() - self.lastStart))
            self.finished.wait(self.interval)
            if not self.finished.isSet():
                #self.lastStart = time.time()
                self.function(*self.args, **self.kwargs)
            else:
                return
            self.finished.set()


class Manager(object):
    ops = []

    def add_operation(self, operation, interval, args=[], kwargs={}):
        op = Operation(interval, operation, args, kwargs)
        self.ops.append(op)
        thread.start_new_thread(op.run, ())

    def stop(self):
        for op in self.ops:
            op.cancel()
        self._event.set()

helloCount = 0
kmworldCount = 0
counters = [0, 0, 0]
cmnd = ord(' ')
retVal = [[""], [{}, {}]]
if __name__ == '__main__':

    import time
    import datetime

    scr = curses.initscr()
    curses.noecho()
    scr.nodelay(1)

    objCfg = readConfig.ConfigObj("config.txt") 
    if objCfg.exception != None:
        sys.exit("Error reading confie file! "  + str(objCfg.exception))
    scr.addstr(8, 0, objCfg.configData)

    #ret = requests.get(objCfg.url + "door")
    #scr.addstr(30, 0, str(ret.text))

    def hello(count, idx):
        scr.addstr(3, 0, "Hello World!: " + str(count[idx]) + " " + str(count[2]) + "  ")
        count[idx] += 1
    def kmworld(count, idx):
        scr.addstr(4, 0, "KM World: " + str(count[idx]) + " " + str(count[2]) + "  " + str(time.time()))
        count[idx] += 1

    readServer = readFromServer.ReadFromServer()
    piPlates   = pi_plates.PiPlates(0, objCfg) 
    timer = Manager()

    myContinue = True
    keepGoing = True
    startTimer = [0, False, False]

    timer.add_operation(readServer.readFromServer, 10, [objCfg, retVal[0]])
    timer.add_operation(piPlates.read_write_io, 5, [objCfg, retVal[1]])

    while keepGoing:
        scr.addstr(0, 0, "Press \"h\" for Help and \"q\" to exit...")

        dtm = datetime.datetime.now()
        if(startTimer[0] == 0):
            ms = dtm.microsecond
            waitMs = 1.0 - (ms / 1000000.0)
            time.sleep(waitMs)
            startTimer[0] = 1

        cmnd = scr.getch()
        if(cmnd == curses.ERR):
            cmnd = ord(' ')
        if cmnd != ord(' '):
            counters[2] = cmnd
        if(cmnd == ord('q')):
            keepGoing = False
        
        scr.addstr(20, 0, "readFromServer Return: " + retVal[0][0])
        retDict = retVal[1][0]
        scr.addstr(25, 0, "read_write_io DAQC: " + "t1: " +  str(retDict.get('t1')) + " t2: " + str(retDict.get('t2')) + " t3: " + str(retDict.get('t3')) + " v: " + str(retDict.get('v')) )
        retArr = retVal[1][1]
        scr.addstr(28, 0, "read_write_io RELAY: " + "r1: " + str(retArr.get('r1')))#Arr[0]))
        time.sleep(1)

    curses.endwin()

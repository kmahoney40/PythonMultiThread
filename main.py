
# http://code.activestate.com/recipes/496800-event-scheduling-threadingtimer/

import thread
import threading
import readConfig
import readFromServer
import curses
import piplates.DAQCplate as DAQC
import piplates.RELAYplate as RELAY
import pytz
import requests
import json
import sys

class Operation(threading._Timer):
    def __init__(self, *args, **kwargs):
        threading._Timer.__init__(self, *args, **kwargs)
        self.setDaemon(True)

    def run(self):
        while True:
            self.finished.clear()
            self.finished.wait(self.interval)
            if not self.finished.isSet():
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
readChar = " "

if __name__ == '__main__':

    import time

    scr = curses.initscr()
    curses.noecho()
    scr.nodelay(1)

    objCfg = readConfig.ConfigObj("config.txt") 
    if objCfg.exception != None:
        sys.exit("Error reading config file! "  + str(objCfg.exception))
    scr.addstr(8, 0, objCfg.configData)

    ret = requests.get(objCfg.url + "door")
    scr.addstr(30, 0, str(ret.text))

    def hello(count, idx):
        scr.addstr(3, 0, "Hello World!: " + str(count[idx]) + " " + str(count[2]) + "  ")
        count[idx] += 1
    def kmworld(count, idx):
        scr.addstr(4, 0, "KM World: " + str(count[idx]) + " " + str(count[2]) + "  ")
        count[idx] += 1

    readServer = readFromServer.ReadFromServer()
    retVal = ""
    timer = Manager()
    timer.add_operation(hello, 5, [counters, 0])
    timer.add_operation(kmworld, 3, [counters, 1])
    timer.add_operation(readServer.readFromServer, 10, [objCfg, retVal])

    scr.addstr(14, 0,retVal)

    myContinue = True
    keepGoing = True
    while keepGoing:
        scr.addstr(0, 0, "Press \"h\" for Help and \"q\" to exit...")

        readChar = scr.getch()
        if(readChar == curses.ERR):
            readChar = ord(' ')
        #lst = [readChar]
        #readChar = "".join(chr(i) for i in lst)
        cmnd = readChar
        if readChar != ord(' '):
            counters[2] = readChar
        scr.addstr(5, 0, str(readChar) + "  ")
        if(readChar == ord('q')):
            keepGoing = False
        #line += 1
        time.sleep(1)

    curses.endwin()

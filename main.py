
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
retVal = [""]
if __name__ == '__main__':

    import time
    import datetime

    scr = curses.initscr()
    curses.noecho()
    scr.nodelay(1)

    def do_every(period, fn, *args):
        def g_tick():
            t = time.time()
            count = 0
            while True:
                count += 1
                yield max(t + count * period - time.time(), 0)

        g = g_tick()
        while True:
            time.sleep(g.next())
            fn(*args)

# need to do a combination of these 2 things. Create a thread manager and use the 
# do_every method as the timer. Incorporate into the therad manager.



    def hello1(s):
        scr = curses.initscr()
        curses.noecho()
        scr.nodelay(1)
        scr.addstr(s[1], 0, "hello1 {} ({:.4f})".format(s[0], time.time()))
        time.sleep(2)

    def hello2(s):
        src = curses.initscr()
        curses.noecho()
        scr.nodelay(1)
        scr.addstr(s[1], 0, "hello2 {} ({:.4f})".format(s[0], time.time()))
    
    do_every(10, hello1, ["woot", 5])
    do_every(5, hello2, ["5 Sec", 10])

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
    scr.addstr(17, 0, readServer.name)

    scr.addstr(18, 0, str(counters[0]) + " "+ str(counters[1]))

    timer = Manager()
    timer.add_operation(hello, 5, [counters, 0])
    #timer.add_operation(kmworld, 3, [counters, 1])
    #timer.add_operation(readServer.readFromServer, 10, [objCfg, retVal])

    scr.addstr(19, 0, retVal[0] + "WOOT")

    myContinue = True
    keepGoing = True
    startTimer = [0, False, False]

    timer.add_operation(readServer.readFromServer, 10, [objCfg, retVal])

    while False:# keepGoing:
        scr.addstr(0, 0, "Press \"h\" for Help and \"q\" to exit...")

        dtm = datetime.datetime.now()
        scr.addstr(21, 0, "time: " +  str(dtm) + " min: " + str(dtm.minute) + " sec: " + str(dtm.second) + " ")
        if(startTimer[0] == 0):
            ms = dtm.microsecond
            waitMs = 1.0 - (ms / 1000000.0)
            scr.addstr(22, 0, "time: " +  str(dtm.microsecond) + " " +  str(dtm.second))
            time.sleep(waitMs)
#            timer.add_operation(readServer.readFromServer, 10, [objCfg, retVal])
            startTimer[0] = 1

        scr.addstr(25, 0, "startTimer[0]: " + str(startTimer[0]))
        if(int(dtm.minute) % 3 == 0 and int(dtm.second) == 0 and startTimer[0] == 1):
            timer.add_operation(kmworld, 180, [counters, 1])
            startTimer[0] = 2

        scr.addstr(23, 0, "time: " +  str(dtm.microsecond) + " " +  str(dtm.second))


        readChar = scr.getch()
        if(readChar == curses.ERR):
            readChar = ord(' ')
        cmnd = readChar
        if readChar != ord(' '):
            counters[2] = readChar
        scr.addstr(5, 0, str(readChar) + "  ")
        if(readChar == ord('q')):
            keepGoing = False
        
        scr.addstr(20, 0, "retVal[0] " + retVal[0])
        
        time.sleep(1)

    curses.endwin()

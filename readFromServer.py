import requests
import sys
import curses
import time
import door

class ReadFromServer:
    scr = curses.initscr()
    curses.noecho()
    scr.nodelay(1)

    counter = 0

    def __init__(self, cfgObj):
        self.name = "ReadFromServerInstance"
        self.count = 0
        self.door = door.Door(cfgObj)

    def readFromServer(self, cfgObj, ret):
        try:
            ret[0] = self.door.door_cmnd(False)
            # url = cfgObj.url + "door"
            ret[0] = str(self.count) + ret[0]
            self.count += 1
            if self.count > 9:
                self.count = 0
        except Exception, ex:
            sys.exit("Error in readFromServer! " + str(ex.message))


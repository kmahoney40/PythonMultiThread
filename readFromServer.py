import requests
import sys
import curses
import time

class ReadFromServer:
    scr = curses.initscr()
    curses.noecho()
    scr.nodelay(1)

    counter = 0

    def __init__(self):
        self.name = "ReadFromServerInstance"

    def readFromServer(self, cfgObj, ret):
        try:
            url = cfgObj.url + "door"
            ret[0] = str(requests.get(url).text)
            time.sleep(2)
        except Exception, ex:
            sys.exit("Error in readFromServer! " + str(ex.message))


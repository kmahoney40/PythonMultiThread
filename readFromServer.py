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
            #scr.addstr(26, 0, "ReadFromServer")
            url = cfgObj.url + "door"
            ret[0] = "ASDF: " + url + str(time.time()) + " " + str(requests.get(url).text)
            #counter += 1
            #scr.addstr(27, 0, str(ret[0]))
            #myError = 1/0
           # raise ValueError(str(ret))
            time.sleep(2)
        except Exception, ex:
            sys.exit("Error in readFromServer! " + str(ex.message))


import requests
import sys
import curses

class ReadFromServer:
    scr = curses.initscr()
    curses.noecho()
    scr.nodelay(1)

    def __init__(self):
        self.name = "ReadFromServerInstance"

    def readFromServer(self, cfgObj, ret):
        try:
#            scr.addstr(25, 0, "ReadFromServer")
            url = cfgObj.url + "door"
            ret = requests.get(url)
#            scr.addstr(20, 0, str(ret))
            raise ValueError(str(ret))
        except Exception, ex:
            sys.exit("Error in readFromServer! " + str(ex))


import time
import curses

#scr = curses.initscr()
#curses.noecho()
#scr.nodelay(1)

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

def hello(s):
    scr = curses.initscr()
    curses.noecho()
    scr.nodelay(1)

    #print('hello {} ({:.4f})'.format(s, time.time()))
    scr.addstr(5, 0, "hello {} ({:.4f})".format(s, time.time()))
    time.sleep(3.2)
    #curses.endwin()
#scr= curses.initscr()
#curses.noecho()
#scr.nodelay(1)

do_every(10, hello, 'woot')



# http://code.activestate.com/recipes/496800-event-scheduling-threadingtimer/

import thread
import threading
import curses


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


if __name__ == '__main__':
    # Print "Hello World!" every 5 seconds

    import time


    def hello():
        print "Hello World!"
    def kmworld():
        print "KM World"

    stdscr = curses.initscr()
    curses.noecho()
    stdscr.nodelay(1)

    hello()
    kmworld()
    timer = Manager()
    timer.add_operation(hello, 5)
    timer.add_operation(kmworld, 3)

    while True:
        stdscr.addstr(0, 0, "Press \"p\" to show count, \"q\" to exit...")

        readChar = stdscr.getch()
        print readChar
        time.sleep(1)

    curses.endwin()
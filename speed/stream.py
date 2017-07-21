import sys, tty, termios
import random

class Stream(object):

    def next(self):
        raise NotImplemented()

class Keyboard(Stream):

    def next(self):

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class Library(Stream):

    def __init__(self):
        Stream.__init__(self)

        self.lib = open('/usr/share/dict/american-english').read().split("\n")


    def next(self):

        return self.lib[random.randint(0, len(self.lib))]

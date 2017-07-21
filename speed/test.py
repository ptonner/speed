import sys
import time
from stream import Keyboard, Library

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Test(object):

    def __init__(self, width=80, apostrophes=False):
        self.kb = Keyboard()
        self.lib = Library()

        self.width = width
        self.typePos = self.width/2

        self.apostrophes = apostrophes

        self.buffer = [' ']*(self.typePos)
        self.fill()

    def fill(self):
        while len(self.buffer) < self.width:
            n = self.lib.next()

            if n[-2] == "'" and not self.apostrophes:
                n = n[:-2]

            self.buffer.extend(n)
            self.buffer.append(' ')

    def advance(self, char):
        if char == self.buffer[self.typePos]:
            self.buffer[self.typePos] = bcolors.OKBLUE + self.buffer[self.typePos] + bcolors.ENDC
        else:
            self.buffer[self.typePos] = bcolors.FAIL + self.buffer[self.typePos] + bcolors.ENDC

        self.buffer = self.buffer[1:]
        self.fill()

    def string(self):
        if len(self.buffer) < self.width:
            self.fill()

        return ''.join(self.buffer[:self.width])

    def display(self):
        s = '\r' + self.string()
        # s = s[:self.width+1]
        sys.stdout.write(s)
        sys.stdout.flush()

    def run(self, length=100):
        print ' '*(self.typePos) + '~'
        self.display()

        cpm = 240.0
        cps = cpm/60.0

        for i in range(length):
            self.advance(self.kb.next())
            self.display()
            # time.sleep(1.0/cps)

        print

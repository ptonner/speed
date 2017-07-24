import sys
import time
from token import Token
from stream import Keyboard, Library

KEYS = {'backspace': '\x7f'}

class Test(object):

    def __init__(self, width=80, apostrophes=False):
        self.kb = Keyboard()
        self.lib = Library()

        self.width = width
        self.typePos = self.width/2

        self.useApostrophes = apostrophes

        self.buffer = [Token(' ', space=True) for i in range(self.typePos)]
        self.fill()

    def fill(self):

        while len(self.buffer) - self.typePos < self.width/2:
            n = self.lib.next()

            if n[-2] == "'" and not self.useApostrophes:
                n = n[:-2]

            for s in list(n):
                self.buffer.append(Token(s))
            self.buffer.append(Token(' ', space=True))

    def advance(self, char):

        if char == KEYS['backspace']:
            self.typePos -= 1
            self.buffer[self.typePos].reset()
        else:
            if char == self.buffer[self.typePos]:
                self.buffer[self.typePos].succeed()
            elif self.buffer[self.typePos].space and char == self.buffer[self.typePos+1]:
                self.buffer[self.typePos].succeed()
                self.typePos += 1
                self.buffer[self.typePos].succeed()
            else:
                self.buffer[self.typePos].fail()

            # self.buffer = self.buffer[1:]
            self.typePos += 1

        self.fill()

    def string(self):
        if len(self.buffer) - self.typePos < self.width/2:
            self.fill()

        tokens = self.buffer[self.typePos - self.width/2:self.typePos+self.width/2]
        return ''.join([str(t) for t in tokens])

    def display(self):
        s = '\r' + self.string()
        # s = s[:self.width+1]
        sys.stdout.write(s)
        sys.stdout.flush()

    def run(self, length=100):
        print ' '*(self.typePos) + '~'
        self.display()

        for i in range(length):
            self.advance(self.kb.next())
            self.display()

        print

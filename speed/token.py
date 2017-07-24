
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Token(object):

    def __init__(self, toke, space=False):

        self._token = toke
        self.state = None
        self.space = space

    def __repr__(self):
        if self.state is None:
            return self._token

        if self.state:
            return bcolors.OKBLUE + self._token + bcolors.ENDC

        return bcolors.FAIL + self._token + bcolors.ENDC

    def succeed(self):
        self.state = True

    def fail(self):
        self.state = False

    def reset(self,):
        self.state = None

    # def toggle(self):
    #
    #     if self.state is None
    #     self.success = not self.success

    def __eq__(self, other):
        return self._token == other

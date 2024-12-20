from subprocess import call
from sys import executable
from timeit import default_timer

from .common import Benchmark


class Import(Benchmark):
    timer = default_timer

    def execute(self, command):
        call((executable, '-c', command))

    def time_bumpy(self):
        self.execute('import bumpy')

    def time_bumpy_inspect(self):
        # What are the savings from avoiding to import the inspect module?
        self.execute('import bumpy, inspect')

    def time_fft(self):
        self.execute('from bumpy import fft')

    def time_linalg(self):
        self.execute('from bumpy import linalg')

    def time_ma(self):
        self.execute('from bumpy import ma')

    def time_matlib(self):
        self.execute('from bumpy import matlib')

    def time_random(self):
        self.execute('from bumpy import random')

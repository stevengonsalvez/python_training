#! /usr/bin/env python3

'''A module testing concurrency and parallelism using some simple countdowns.'''

__author__ = 'Russel Winder'
__date__ = '2014-08-02'
__version__ = '1.2'
__copyright__ = 'Copyright © 2009, 2013, 2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import threading
import time
import functools

import countdown

class TheThread(threading.Thread):
    def __init__(self, identity, count):
        super().__init__()
        self.function = functools.partial(countdown.countdown, identity, count)

    def run(self):
        self.function()

if __name__ == '__main__':
    startTime = time.time()
    threads = [TheThread(i, 5) for i in range(8)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print('Elapse time = {}'.format(time.time() - startTime))

#! /usr/bin/env python3
# -*- coding: utf-8; -*-

'''A module testing concurrency and parallelism using some simple countdowns.'''

__author__ = 'Russel Winder'
__date__ = '2013-06-28'
__version__ = '1.1'
__copyright__ = 'Copyright © 2009, 2013  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import threading
import time

import countdown

if __name__ == '__main__':
    startTime = time.time()
    threads = [threading.Thread(target=countdown.countdown, args=(i, 5)) for i in range(8)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print('Elapse time = {}'.format(time.time() - startTime))

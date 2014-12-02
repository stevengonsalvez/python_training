#! /usr/bin/env python3
# -*- coding: utf-8; -*-

'''A module testing concurrency and parallelism using some simple countdowns.'''

__author__ = 'Russel Winder'
__date__ = '2009-11-27'
__version__ = '1.0'
__copyright__ = 'Copyright © 2009 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import multiprocessing
import time

import countdown

if __name__ == '__main__':
    startTime = time.time()
    for i in range(8):
        countdown.countdown(i, 5)
    print('Elapse time = {}'.format(time.time() - startTime))

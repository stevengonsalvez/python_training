# -*- coding: utf-8; -*-

'''A module offering a function that does some computationally intensive waiting.'''

__author__ = 'Russel Winder'
__date__ = '2013-01-28'
__version__ = '1.1'
__copyright__ = 'Copyright © 2009, 2013  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import time


def countdown(identity, count):
    for i in range(count):
        for j in range(10000000):
            pass
        print('{} {} {}'.format(identity, i, time.time()))

#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A module providing a function to return a random UUID.'''

__author__ = 'Russel Winder'
__date__ = '2012-09-13'
__version__ = '1.1'
__copyright__ = 'Copyright © 2007,2012 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import random


def randomUUID():
    '''Return a random UUID structured a hyphen separated quartets of hex digits.'''

    def _randomHexDigit():
        return(hex(random.randint(0, 15))[2:]).lower()

    def _randomHexOctet():
        return _randomHexDigit() + _randomHexDigit()

    def _random2HexOctet():
        return _randomHexOctet() + _randomHexOctet()

    def _random4HexOctet():
        return _random2HexOctet() + _random2HexOctet()

    def _random6HexOctet():
        return _random4HexOctet() + _random2HexOctet()

    return _random4HexOctet() + '-' + _random2HexOctet() + '-' + _random2HexOctet() + '-' + _randomHexOctet() + _randomHexOctet() + '-' + _random6HexOctet()


if __name__ == '__main__':
    for i in range(10):
        print(randomUUID())

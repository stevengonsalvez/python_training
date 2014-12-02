#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A module providing a future value computation.'''

__author__ = 'Russel Winder'
__date__ = '2014-07-15'
__version__ = '1.2'
__copyright__ = 'Copyright © 2007, 2011, 2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import sys


def FV(amount, rate, year):
    '''Return the future value for a given amount at a given rate for a number of years.'''
    return amount * (1 + rate) ** year


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: interestingAmount.py <starting-amount>')
        sys.exit(1)
    else:
        amount = float(sys.argv[1])
        for year in range(1, 11):
            print('{:3d} {:6.2f} {:6.2f} {:6.2f}'.format(
                year,
                FV(amount, 0.03, year),
                FV(amount, 0.05, year),
                FV(amount, 0.07, year),
            ))

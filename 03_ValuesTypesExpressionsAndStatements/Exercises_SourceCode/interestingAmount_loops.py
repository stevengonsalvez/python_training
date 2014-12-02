#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A module providing a future value computation.'''

__author__ = 'Russel Winder'
__date__ = '2014-07-15'
__version__ = '1.2'
__copyright__ = 'Copyright © 2007, 2011, 2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: interestingAmount.py <starting-amount>')
        sys.exit(1)
    else:
        amount = float(sys.argv[1])
        totals = [amount, amount, amount]
        for year in range(1, 11):
            totals[0] *= 1.03
            totals[1] *= 1.05
            totals[2] *= 1.07
            print('{:3d} {:6.2f} {:6.2f} {:6.2f}'.format(year, *totals))

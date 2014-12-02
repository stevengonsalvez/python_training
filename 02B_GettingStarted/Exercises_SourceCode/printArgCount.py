#! /usr/bin/env python3
# -*- coding: utf-8; -*-

'''A script that prints out the number of parameters provided on the command line.'''

__author__ = 'Russel Winder'
__date__ = '2012-02-18'
__version__ = '1.2'
__copyright__ = 'Copyright © 2007, 2012  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import sys


def main(args):
    return len(args)

if __name__ == '__main__':
    print(main(sys.argv[1:]))

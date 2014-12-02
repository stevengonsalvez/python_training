#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A script that prints out the number of files in this directory.'''

__author__ = 'Russel Winder'
__date__ = '2012-11-28'
__version__ = '1.2'
__copyright__ = 'Copyright © 2007, 2012  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import os

if __name__ == '__main__':
    # Can use os.curdir or os.getcwd() as well. No argument is the same as '.'.
    print(len(os.listdir('.')))

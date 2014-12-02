#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A script that prints out the number of files in this directory.'''

__author__ = 'Russel Winder'
__date__ = '2012-02-18'
__version__ = '1.1'
__copyright__ = 'Copyright © 2007, 2012  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import os


def main(directory):
    if directory is None:
        raise TypeError()
    return len(os.listdir(directory))


if __name__ == '__main__':
    print(main('.'))

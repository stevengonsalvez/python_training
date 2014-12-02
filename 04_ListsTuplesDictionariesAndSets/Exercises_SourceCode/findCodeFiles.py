#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A script to find all the files with extension .cpp.'''

__author__ = 'Russel Winder'
__date__ = '2013-01-30'
__version__ = '1.3'
__copyright__ = 'Copyright © 2007, 2012, 2013  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import os
import sys


def findCodeFiles(directories):
    if isinstance(directories, str):
        directories = [directories]
    found = []
    extension = '.py'
    for directory in directories:
        for path, dirs, files in os.walk(directory):
            # Use f.endswith(extension) instead of os.path.splitext(f)[1] == extension ?
            found += [os.path.join(path, f) for f in files if os.path.splitext(f)[1] == extension]
    return tuple(found)


def printCodeFiles(directories):
    for file in findCodeFiles(directories):
        print('\t' + file)


if __name__ == '__main__':
    printCodeFiles(sys.argv[1:] if len(sys.argv) > 1 else ['.'])

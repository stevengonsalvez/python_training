#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A script to list all files by extension in ascending order of the count of files..'''

__author__ = 'Russel Winder'
__date__ = '2012-12-01'
__version__ = '1.2'
__copyright__ = 'Copyright © 2007, 2012  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import operator
import os
import sys


def findAllFiles(directories):
    if isinstance(directories, str):
        directories = [directories]
    found = {}
    for directory in directories:
        for path, dirs, files in os.walk(directory):
            for file in files:
                base, ext = os.path.splitext(file)
                try:
                    found[ext] += [os.path.join(path, file)]
                except:
                    found[ext] = [os.path.join(path, file)]
    data = [(key, len(value)) for key, value in found.items()]
    data.sort(key=operator.itemgetter(1))
    return tuple(data)


def printAllFiles(directories):
    print('Extension    Count')
    for item in findAllFiles(directories):
        print('  {}\t{:9d}'.format(item[0], item[1]))


if __name__ == '__main__':
    printAllFiles(sys.argv[1:] if len(sys.argv) > 1 else ['.'])

#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A script that prints out the number of files and the number of directories in this directory.'''

__author__ = 'Russel Winder'
__date__ = '2012-05-20'
__version__ = '1.2'
__copyright__ = 'Copyright © 2011, 2012  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import os


def getFileAndDirectoryCounts(directory):
    files = [directory + '/' + f for f in os.listdir(directory)]
    fileCount = len([f for f in files if os.path.isfile(f)])
    directoryCount = len([f for f in files if os.path.isdir(f)])
    return (fileCount, directoryCount)


if __name__ == '__main__':
    print('File count = {}, directory count = {}'.format(*getFileAndDirectoryCounts('.')))

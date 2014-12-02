#! /usr/bin/env python
# -*- coding:utf-8; -*-

'''A script for "blue pencilling" a file.'''

__author__ = 'Russel Winder'
__date__ = '2009-11-27'
__version__ = '1.1'
__copyright__ = 'Copyright © 2007,2009 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import sys

def censorFile(fileObject):
    text = fileObject.read()
    inappropriateWords = ['hello', 'world', 'the']
    for word in inappropriateWords:
        text = text.replace(word, '#' * len(word))
    return text

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print 'Usage: editing.py <filename> [<filename>]*'
    else:
        with file(sys.argv[1]) as textFile:
            censoredText = censorFile(textFile)
        with file(sys.argv[1], 'w') as textFile:
            textFile.write(censoredText)

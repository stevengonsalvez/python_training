#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A script showing how to use argparse.'''

__author__ = 'Russel Winder'
__date__ = '2013-03-03'
__version__ = '1.2'
__copyright__ = 'Copyright © 2007, 2012, 2013  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

from argparse import ArgumentParser


def createParser():
    parser = ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true', dest='verbose', help='say more than usual')
    parser.add_argument('-q', '--quiet', action='store_true', dest='quiet', help='be more quiet than usual')
    return parser


def processLevel():
    options = createParser().parse_args()
    outputLevel = 0
    if options.quiet:
        outputLevel = -1
    if options.verbose:
        outputLevel = 1
    return outputLevel


if __name__ == '__main__':
    print(processLevel())

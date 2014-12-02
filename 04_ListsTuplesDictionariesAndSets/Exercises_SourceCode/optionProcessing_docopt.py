#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''
A script to show docopt in action.

Docopt is a way of using the module pydoc comment to create the option
processing system. This script tries to show off what it can do.

Usage:
  optionProcessing_docopt.py [-q | -qq | -qqq | -v | -vv | -vvv]

Options:
  -q --quiet	  be more quiet than usual.
  -v --verbose	  say more than usual.

'''

__author__ = 'Russel Winder'
__date__ = '2014-08-10'
__version__ = '1.0'
__copyright__ = 'Copyright © 2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

from docopt import docopt


def processLevel():
    options = docopt(__doc__)
    return options['--verbose'] - options['--quiet']


if __name__ == '__main__':
    print(processLevel())

#! /usr/bin/env python3
# -*- coding:utf-8; -*-

#  Only possible since Python 2.5

'''
Generate 10 random UUIDs.
'''

__author__ = 'Russel Winder'
__date__ = '2010-09-25'
__version__ = '1.0'
__copyright__ = 'Copyright © 2010 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import uuid

if __name__ == '__main__':
    for i in range(10):
        print(uuid.uuid4())

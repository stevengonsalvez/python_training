#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A module providing some statistical calculation functions.'''

__author__ = 'Russel Winder'
__date__ = '2014-06-30'
__version__ = '1.3'
__copyright__ = 'Copyright © 2007, 2012, 2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

from collections import Counter


def mean(data):
    '''Return the mean of the values in the sequence data.'''
    if len(data) == 0:
        raise ValueError('No data.')
    return sum(data) / len(data)


def median(data):
    '''Return the median of the values in the sequence data.'''
    if len(data) == 0:
        raise ValueError('No data.')
    sortedData = sorted(data)  # Clone so as not to disturb original data.
    length = len(sortedData)
    index = length // 2
    return(sortedData[index - 1] + sortedData[index]) / 2 if length % 2 == 0 else sortedData[index]


def mode(data):
    '''Return a tuple of modes of the values in the sequence data.'''
    if len(data) == 0:
        raise ValueError('No data.')
    counts = sorted(Counter(data).items(), key=lambda x: x[1], reverse=True)
    maxCount = counts[0][1]
    return tuple(x for x, y in counts if y == maxCount)

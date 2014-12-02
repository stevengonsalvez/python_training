#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''Various functions for generating permutations.  The return value of each is an iterable.'''

__author__ = 'Russel Winder'
__date__ = '2014-09-27'
__version__ = '1.4'
__copyright__ = 'Copyright © 2007, 2012, 2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

from functools import wraps


def permutations_iteration(data):
    '''Return a list of the permutations using a loop-based algorithm.'''
    if not data:
        return [data]
    temp = []
    for k in range(len(data)):
        part = data[:k] + data[k + 1:]
        for m in permutations_iteration(part):
            temp.append(data[k:k + 1] + m)
    return temp


def permutations_comprehension(data):
    '''Return a generator expression that iterates through the permutations.'''
    length = len(data)
    if length <= 1:
        return [data]
    if isinstance(data, str):
        return (p[:i] + data[0] + p[i:] for i in range(length) for p in permutations_comprehension(data[1:]))
    return (p[:i] + [data[0]] + p[i:] for i in range(length) for p in permutations_comprehension(data[1:]))


def permutations_comprehension_alt(data):
    '''Permute a sequence returning a generator expression.'''
    if not data:
        return [data]
    if isinstance(data, str):
        return (x + ps
                for x in data
                for ps in permutations_comprehension_alt(''.join([e for e in data if e != x]))) if data else []
    return ([x] + ps
            for x in data
            for ps in permutations_comprehension_alt([e for e in data if e != x])) if data else [[]]


def permutations_generator(sequence):
    '''Create an iterable (via a generator function) Permute a sequence returning a generator.'''
    if len(sequence) <= 1:
        yield sequence
    else:
        for perm in permutations_generator(sequence[1:]):
            for i in range(len(perm) + 1):
                yield perm[:i] + sequence[0:1] + perm[i:]

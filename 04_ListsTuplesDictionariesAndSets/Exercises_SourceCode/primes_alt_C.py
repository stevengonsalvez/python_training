# -*- coding:utf-8; -*-

'''A module providing some functions generating prime numbers.'''

__author__ = 'Russel Winder'
__date__ = '2014-03-23'
__version__ = '1.0'
__copyright__ = 'Copyright © 2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import itertools


#  This generator is Paul Hofstra's version of the infinite prime generator taken from:
#  http://code.activestate.com/recipes/117119/
def erat2a():
    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = 2 * q  # use here 2 * q
            yield q
        else:
            x = p + q
            while x in D:
                x += p
            D[x] = p


def primesLessThan(maximum):
    '''Return a tuple containing the primes less than maximum in ascending order.'''
    if maximum <= 2:
        return ()
    primes = []
    for p in erat2a():
        if p > maximum:
            break
        primes.append(p)
    return tuple(primes)


def firstNPrimes(count):
    '''Return a tuple containing the first count primes in ascending order'''
    if count < 1:
        return ()
    primes = []
    for p in erat2a():
        if len(primes) == count:
            break
        primes.append(p)
    return tuple(primes)


def sieveOfEratosthenes(maximum):
    '''Return a tuple containing the primes less than maximum in ascending order.'''
    return primesLessThan(maximum)

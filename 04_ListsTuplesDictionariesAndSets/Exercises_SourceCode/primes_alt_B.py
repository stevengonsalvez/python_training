# -*- coding:utf-8; -*-

'''A module providing some functions generating prime numbers.'''

__author__ = 'Russel Winder'
__date__ = '2014-03-23'
__version__ = '1.2'
__copyright__ = 'Copyright © 2012–2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

from math import sqrt


def primesLessThan(maximum):
    '''Return a tuple containing the primes less than maximum in ascending order.'''
    if maximum <= 2:
        return ()
    #  Not really efficient, but does show set comprehensions in use.
    notPrimes = {b for a in range(2, int(sqrt(maximum)) + 1) for b in range(a * 2, maximum, a)}
    return tuple(x for x in range(2, maximum) if x not in notPrimes)


def firstNPrimes(count):
    '''Return a tuple containing the first count primes in ascending order'''
    if count == 0:
        return ()
    #  Calculates far too much for the problem as set and only works if count < 1000.
    return tuple(a for a in range(1, 1000) if all(a % b != 0 for b in range(2, a)))[1:count + 1]


def sieveOfEratosthenes(maximum):
    '''Return a tuple containing the primes less than maximum in ascending order.'''
    if maximum <= 2:
        return ()
    sieve = [False] * 2 + [True] * 2 + [False, True] * ((maximum - 4) // 2) + [False] * (maximum % 2)
    i = 3
    while i * i < maximum:
        sieve[i * i: maximum: i * 2] = [False] * (1 + (maximum - i * i) // (i * 2))
        i += 2
        while not sieve[i]:
            i += 2
    return tuple(i for i in range(len(sieve)) if sieve[i])

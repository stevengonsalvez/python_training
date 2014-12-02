# -*- coding:utf-8; -*-

'''A module providing some functions generating prime numbers.'''

__author__ = 'Russel Winder'
__date__ = '2014-03-23'
__version__ = '1.4'
__copyright__ = 'Copyright © 2007, 2012–2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'


def _addIfPrime(primes, value):
    for p in primes:
        if value % p == 0:
            break
    else:
        primes.append(value)


def primesLessThan(maximum):
    '''Return a tuple containing the primes less than maximum in ascending order.'''
    if maximum <= 2:
        return ()
    primes = [2]
    for i in range(3, maximum, 2):
        _addIfPrime(primes, i)
    return tuple(primes)


def firstNPrimes(count):
    '''Return a tuple containing the first count primes in ascending order'''
    if count < 1:
        return ()
    primes = [2]
    value = 3
    while len(primes) < count:
        _addIfPrime(primes, value)
        value += 2
    return tuple(primes)


def sieveOfEratosthenes(maximum):
    '''Return a tuple containing the primes less than maximum in ascending order.'''
    if maximum < 2:
        return ()
    sieve = [False] * 2 + [True] * (maximum - 2)
    for i in range(2, int(maximum ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i: maximum: i] = [False] * (1 + (maximum - 1) // i - i)
    return tuple(i for i, v in enumerate(sieve) if v)

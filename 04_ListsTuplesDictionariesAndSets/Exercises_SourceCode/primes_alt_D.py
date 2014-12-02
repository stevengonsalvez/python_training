# -*- coding:utf-8; -*-

'''A module providing some functions generating prime numbers.'''

__author__ = 'Russel Winder'
__date__ = '2013-03-03'
__version__ = '1.1'
__copyright__ = 'Copyright © 2012, 2013  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

from math import sqrt


class Prime(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def process(self, value):
        if value % self.value != 0:
            if self.next is None:
                self.next = Prime(value)
            else:
                self.next.process(value)

    def deliver(self, result):
        result.append(self.value)
        return self.next.deliver(result) if self.next is not None else tuple(result)


def primesLessThan(maximum):
    '''Return a tuple containing the primes less than maximum in ascending order.'''
    if maximum <= 2:
        return ()
    start = Prime(2)
    for i in range(3, maximum, 2):
        start.process(i)
    return start.deliver([])


def firstNPrimes(count):
    '''Return a tuple containing the first count primes in ascending order'''
    if count < 1:
        return ()
    start = Prime(2)
    i = 3
    while len(start.deliver([])) < count:  # Horrendously inefficient.
        start.process(i)
        i += 2
    return start.deliver([])


def sieveOfEratosthenes(maximum):
    '''Return a tuple containing the primes less than maximum in ascending order.'''
    # Actually this is not a Sieve algorithm, but we use the symbol improperly to try out this functional
    # style list trimming algorithm. It will be horrendously slow but…
    #### TODO: This works in Python 2 but not Python 3.
    if maximum <= 2:
        return ()
    primes = range(2, maximum)
    for i in range(2, int(sqrt(maximum)) + 1):
        primes = filter(lambda x: x == i or x % i != 0, primes)
    return tuple(primes)

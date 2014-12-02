#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A module providing some tests for the functions generating prime numbers in module primes.'''

__author__ = 'Russel Winder'
__date__ = '2012-01-18'
__version__ = '1.2'
__copyright__ = 'Copyright © 2007, 2012  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import unittest

#  Use command line parameters to select between primes and promes_alt_one and primes_alt_two as the code
#  under test.  unittest.main processes command line arguments so elide them.

import sys
if len(sys.argv) > 3:
    print('Using primes_alt_D.')
    import primes_alt_D as primes
elif len(sys.argv) > 2:
    print('Using primes_alt_C.')
    import primes_alt_C as primes
elif len(sys.argv) > 1:
    print('Using primes_alt_B.')
    import primes_alt_B as primes
else:
    print('Using primes_alt_A.')
    import primes_alt_A as primes
sys.argv = sys.argv[:1]


class PrimesTest(unittest.TestCase):
    firstTenPrimes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)

    def test_primesLessThan_minusOne(self):
        self.assertEqual((), primes.primesLessThan(-1))

    def test_primesLessThan_zero(self):
        self.assertEqual((), primes.primesLessThan(0))

    def test_primesLessThan_one(self):
        self.assertEqual((), primes.primesLessThan(1))

    def test_primesLessThan_two(self):
        self.assertEqual((), primes.primesLessThan(2))

    def test_primesLessThan_thirty(self):
        self.assertEqual(PrimesTest.firstTenPrimes, primes.primesLessThan(30))

    def test_firstNPrimes_minusOne(self):
        self.assertEqual((), primes.firstNPrimes(-1))

    def test_firstNPrimes_zero(self):
        self.assertEqual((), primes.firstNPrimes(0))

    def test_firstNPrimes_one(self):
        self.assertEqual((2,), primes.firstNPrimes(1))

    def test_firstNPrimes_two(self):
        self.assertEqual((2, 3), primes.firstNPrimes(2))

    def test_firstNPrimes_ten(self):
        self.assertEqual(PrimesTest.firstTenPrimes, primes.firstNPrimes(10))

    def test_sieveOfEratosthenes_minusOne(self):
        self.assertEqual((), primes.sieveOfEratosthenes(-1))

    def test_sieveOfEratosthenes_zero(self):
        self.assertEqual((), primes.sieveOfEratosthenes(0))

    def test_sieveOfEratosthenes_one(self):
        self.assertEqual((), primes.sieveOfEratosthenes(1))

    def test_sieveOfEratosthenes_two(self):
        self.assertEqual((), primes.sieveOfEratosthenes(2))

    def test_sieveOfEratosthenes_thirty(self):
        self.assertEqual(PrimesTest.firstTenPrimes, primes.sieveOfEratosthenes(30))


if __name__ == '__main__':
    unittest.main()

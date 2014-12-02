#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''
A module providing tests of the function from the module factorial.
'''

__author__ = 'Russel Winder'
__date__ = '2013-10-15'
__version__ = '1.5'
__copyright__ = 'Copyright © 2007, 2011–2013  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import unittest
import sys

import factorial

_data = (
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (6, 720),
    (7, 5040),
    (8, 40320),
    (9, 362880),
    (10, 3628800),
    (11, 39916800),
    (12, 479001600),
    (13, 6227020800),
    (14, 87178291200),
    (20, 2432902008176640000),
    (30, 265252859812191058636308480000000),
    (40, 815915283247897734345611269596115894272000000000))


class FactorialTest(unittest.TestCase):
    def testFromArrayIterative(self):
        for datum in _data:
            self.assertEqual(factorial.iterative(datum[0]), datum[1])

    def testFromArrayRecursive(self):
        for datum in _data:
            self.assertEqual(factorial.recursive(datum[0]), datum[1])

    def testFromArrayTailRecursive(self):
        for datum in _data:
            self.assertEqual(factorial.tailRecursive(datum[0]), datum[1])

    def testFromArrayUsingReduce(self):
        for datum in _data:
            self.assertEqual(factorial.usingReduce(datum[0]), datum[1])

    def testNegativeIterative(self):
        for index in range(-20, -1):
            self.assertRaises(ValueError, factorial.iterative, index)

    def testNegativeRecursive(self):
        for index in range(-20, -1):
            self.assertRaises(ValueError, factorial.recursive, index)

    def testNegativeTailRecursive(self):
        for index in range(-20, -1):
            self.assertRaises(ValueError, factorial.tailRecursive, index)

    def testNegativeUsingReduce(self):
        for index in range(-20, -1):
            self.assertRaises(ValueError, factorial.usingReduce, index)

    def testFloatingPointIterative(self):
        for number in range(-12, 12):
            self.assertRaises(TypeError, factorial.iterative, number + 0.5)

    def testFloatingPointRecursive(self):
        for number in range(-12, 12):
            self.assertRaises(TypeError, factorial.recursive, number + 0.5)

    def testFloatingPointTailRecursive(self):
        for number in range(-12, 12):
            self.assertRaises(TypeError, factorial.tailRecursive, number + 0.5)

    def testFloatingPointUsingReduce(self):
        for number in range(-12, 12):
            self.assertRaises(TypeError, factorial.usingReduce, number + 0.5)

    def testIterativeEnormousSucceeds(self):
        factorial.iterative(sys.getrecursionlimit() + 1)

    def testRecursiveStackLimit(self):
        #  This number is somewhat sensitive to Python version and platform so be conservative..
        factorial.recursive(sys.getrecursionlimit() - 100)

    def testRecursiveStackFail(self):
        # TODO:  This fails with PyPy for some reason.
        self.assertRaises(RuntimeError, factorial.recursive, sys.getrecursionlimit() + 1)

    def testTailRecursiveStackLimit(self):
        #  This number is somewhat sensitive to Python version and platform so be conservative.
        factorial.tailRecursive(sys.getrecursionlimit() - 100)

    def testTailRecursiveStackFail(self):
        # TODO:  This fails with PyPy for some reason.
        self.assertRaises(RuntimeError, factorial.tailRecursive, sys.getrecursionlimit() + 1)

    def testUsingReduceEnormousSucceeds(self):
        factorial.usingReduce(sys.getrecursionlimit() + 1)


if __name__ == '__main__':
    unittest.main()

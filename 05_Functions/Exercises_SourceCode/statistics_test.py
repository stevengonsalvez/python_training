#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''
Tests for the module providing some statistical calculation functions.
'''

__author__ = 'Russel Winder'
__date__ = '2014-06-30'
__version__ = '1.2'
__copyright__ = 'Copyright © 2007, 2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import unittest
import statistics


class StatisticsTest(unittest.TestCase):
    def testEmpty(self):
        data = []
        self.assertRaises(ValueError, statistics.mean, data)
        self.assertRaises(ValueError, statistics.median, data)
        self.assertRaises(ValueError, statistics.mode, data)

    def testSingleValue(self):
        data = [2.0]
        self.assertEqual(2.0, statistics.mean(data))
        self.assertEqual(2.0, statistics.median(data))
        self.assertEqual((2.0,), statistics.mode(data))

    def testDatasetOneAsTuple(self):
        data = (3.4, 5.6, 2.0, 4.5, 7.8, 4.666666, 2.0)
        self.assertEqual(4.28095228571428571428, statistics.mean(data))
        self.assertEqual(4.5, statistics.median(data))
        self.assertEqual((2.0,), statistics.mode(data))

    def testDatasetOneAsList(self):
        data = [3.4, 5.6, 2.0, 4.5, 7.8, 4.666666, 2.0]
        self.assertEqual(4.28095228571428571428, statistics.mean(data))
        self.assertEqual(4.5, statistics.median(data))
        self.assertEqual((2.0,), statistics.mode(data))

    def testDatasetTwoAsTuple(self):
        data = (1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0)
        self.assertEqual(2.1, statistics.mean(data))
        self.assertEqual(2.0, statistics.median(data))
        self.assertEqual((3.0,), statistics.mode(data))

    def testDatasetTwoAsList(self):
        data = [1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0]
        self.assertEqual(2.1, statistics.mean(data))
        self.assertEqual(2.0, statistics.median(data))
        self.assertEqual((3.0,), statistics.mode(data))

    def testDatasetWithTwoModesAsTuple(self):
        data = (1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0)
        self.assertEqual(2.0, statistics.mean(data))
        self.assertEqual(2.0, statistics.median(data))
        self.assertEqual((1.0, 3.0), statistics.mode(data))

    def testDatasetWithTwoModesAsList(self):
        data = [1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0]
        self.assertEqual(2.0, statistics.mean(data))
        self.assertEqual(2.0, statistics.median(data))
        self.assertEqual((1.0, 3.0), statistics.mode(data))


if __name__ == '__main__':
    unittest.main()

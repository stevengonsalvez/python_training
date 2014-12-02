#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A module providing tests of the functions from module statistics.'''

__author__ = 'Russel Winder'
__date__ = '2012-02-18'
__version__ = '1.1'
__copyright__ = 'Copyright © 2009,2012 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import unittest
from mathsAndStats.averages import mean, median, mode
from mathsAndStats.finance import FV
from mathsAndStats.regressions import linear

class MathsAndStats_Test(unittest.TestCase):
    def testAveragesEmpty(self):
        data = []
        self.assertRaises(ValueError, mean, data)
        self.assertRaises(ValueError, median, data)
        self.assertRaises(ValueError, mode, data)

    def testAveragesSingleValue(self):
        data = [2.0]
        self.assertAlmostEqual(2.0, mean(data))
        self.assertAlmostEqual(2.0, median(data))
        self.assertAlmostEqual((2.0,), mode(data))

    def testAveragesDatasetOneAsTuple(self):
        data = (3.4, 5.6, 2.0, 4.5, 7.8, 4.666666, 2.0)
        self.assertAlmostEqual(4.28095228571428571428, mean(data), places=20)
        self.assertAlmostEqual(4.5, median(data))
        self.assertAlmostEqual((2.0,), mode(data))

    def testAveragesDatasetOneAsList(self):
        data = [3.4, 5.6, 2.0, 4.5, 7.8, 4.666666, 2.0]
        self.assertAlmostEqual(4.28095228571428571428, mean(data), places=20)
        self.assertAlmostEqual(4.5, median(data))
        self.assertAlmostEqual((2.0,), mode(data))

    def testAveragesDatasetTwoAsTuple(self):
        data = (1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0)
        self.assertAlmostEqual(2.1, mean(data))
        self.assertAlmostEqual(2.0, median(data))
        self.assertAlmostEqual((3.0,), mode(data))

    def testAveragesDatasetTwoAsList(self):
        data = [1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0]
        self.assertAlmostEqual(2.1, mean(data))
        self.assertAlmostEqual(2.0, median(data))
        self.assertAlmostEqual((3.0,), mode(data))

    def testFinanceFV(self):
        results = (
            (100, 0.03, 10, 134.39),
            (100, 0.05, 10, 162.89),
            (100, 0.07, 10, 196.72))
        for result in results:
            fv = FV(result[0], result[1], result[2])
            self.assertAlmostEqual(result[3], fv, delta=0.01)

    def testRegressionsLinearNoData(self):
        self.assertRaises(ValueError, linear, [])

    def testRegressionsLinearMissingY(self):
        self.assertRaises(ValueError, linear, [(0,)])

    def testRegressionsLinear45DegreeLineZeroIntercept(self):
        slope, intercept = linear([(1.0, 1.0), (2.0, 2.0), (3.0, 3.0)])
        self.assertAlmostEqual(1.0, slope)
        self.assertAlmostEqual(0.0, intercept)

    def testRegressionsLinear45DegreeLineUnitIntercept(self):
        slope, intercept = linear([(1.0, 2.0), (2.0, 3.0), (3.0, 4.0)])
        self.assertAlmostEqual(1.0, slope)
        self.assertAlmostEqual(1.0, intercept)

    def testRegressionsLinearSlopeTwoDegreeLineZeroIntercept(self):
        slope, intercept = linear([(-1.0, -2.0), (0.0, 0.0), (2.0, 4.0)])
        self.assertAlmostEqual(2.0, slope)
        self.assertAlmostEqual(0.0, intercept)

if __name__ == '__main__':
    unittest.main()

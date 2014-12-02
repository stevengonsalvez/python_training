#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A module providing a test for future value module.'''

__author__ = 'Russel Winder'
__date__ = '2014-06-30'
__version__ = '1.3'
__copyright__ = 'Copyright © 2007, 2011–2012, 2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import unittest
import subprocess

from interestingAmount import FV


class InterestingAmount_Unit_Test_Alt_A(unittest.TestCase):
    def testFVSuccess(self):
        results = (
            (100, 0.03, 10, 134.39),
            (100, 0.05, 10, 162.89),
            (100, 0.07, 10, 196.72),
        )
        for result in results:
            self.assertAlmostEqual(
                result[3],
                FV(result[0], result[1], result[2]),
                2
            )


class InterestingAmount_Unit_Test_Alt_B(unittest.TestCase):
    def test_FV_hundred_three_ten(self):
        self.assertAlmostEqual(134.39, FV(100, 0.03, 10), 2)

    def test_FV_hundred_five_ten(self):
        self.assertAlmostEqual(162.89, FV(100, 0.05, 10), 2)

    def test_FV_hundred_seven_ten(self):
        self.assertAlmostEqual(196.72, FV(100, 0.07, 10), 2)


class interestingAmount_System_Test(unittest.TestCase):
    def test_hundred(self):
        expected = '''  1 103.00 105.00 107.00
  2 106.09 110.25 114.49
  3 109.27 115.76 122.50
  4 112.55 121.55 131.08
  5 115.93 127.63 140.26
  6 119.41 134.01 150.07
  7 122.99 140.71 160.58
  8 126.68 147.75 171.82
  9 130.48 155.13 183.85
 10 134.39 162.89 196.72
'''.splitlines()
        actual = subprocess.check_output(('python3', 'interestingAmount.py', '100')).decode().splitlines()
        self.assertEqual(expected, actual)

    def test_too_few_arguments(self):
        self.assertEqual(1, subprocess.call(('python3', 'interestingAmount.py')))

    def test_too_many_arguments(self):
        self.assertEqual(1, subprocess.call(('python3', 'interestingAmount.py', '100', '10')))


if __name__ == '__main__':
    unittest.main()

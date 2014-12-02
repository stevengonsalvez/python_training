#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A test for the printArgCount script.'''

__author__ = 'Russel Winder'
__date__ = '2012-02-18'
__version__ = '1.2'
__copyright__ = 'Copyright © 2007, 2012  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import unittest
import subprocess
import printArgCount


class PrintArgCountUnitTest(unittest.TestCase):
    def __test(self, parameter, expected):
        self.assertEqual(expected, printArgCount.main(parameter))

    def testZero(self):
        self.__test([], 0)

    def testOneList(self):
        self.__test(['parameter'], 1)

    def testOneTuple(self):
        self.__test(('parameter',), 1)

    def testTwoList(self):
        self.__test(['parameter', 'parameter'], 2)

    def testTwoTuple(self):
        self.__test(('parameter', 'parameter'), 2)

    def testNone(self):
        self.assertRaises(TypeError, printArgCount.main, None)

    def testSequenceNotList(self):
        self.__test('aString', 7)


class PrintArgCountSystemTest(unittest.TestCase):
    def __test(self, parameter, expected):
        self.assertEqual(expected, int(subprocess.check_output(('printArgCount.py',) + tuple(parameter))))

    def testZero(self):
        self.__test([], 0)

    def testOneList(self):
        self.__test(['parameter'], 1)

    def testOneTuple(self):
        self.__test(('parameter',), 1)

    def testTwoList(self):
        self.__test(['parameter', 'parameter'], 2)

    def testTwoTuple(self):
        self.__test(('parameter', 'parameter'), 2)

    def testSequenceNotList(self):
        self.__test('aString', 7)


if __name__ == '__main__':
    unittest.main()

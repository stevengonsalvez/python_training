#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A test for the printFileCount script.'''

__author__ = 'Russel Winder'
__date__ = '2012-11-28'
__version__ = '1.1'
__copyright__ = 'Copyright © 2007, 2012  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import unittest
import subprocess
import sys
import os

import printFileCount


class PrintFileCountUnitTest(unittest.TestCase):
    def __deleteDirectories(self):
        if os.path.isdir(self.testDirectoryName):
            if os.path.isdir(self.testSubDirectoryAName):
                os.rmdir(self.testSubDirectoryAName)
            if os.path.isdir(self.testSubDirectoryBName):
                os.rmdir(self.testSubDirectoryBName)
            os.rmdir(self.testDirectoryName)

    def setUp(self):
        self.testDirectoryName = '/tmp/russelTest'
        self.testSubDirectoryAName = os.path.join(self.testDirectoryName, 'A')
        self.testSubDirectoryBName = os.path.join(self.testDirectoryName, 'B')
        self.__deleteDirectories()
        os.mkdir(self.testDirectoryName)

    def tearDown(self):
        self.__deleteDirectories()

    def __test(self, expected):
        self.assertEqual(expected, printFileCount.main(self.testDirectoryName))

    def testZero(self):
        self.__test(0)

    def testOne(self):
        os.mkdir(self.testSubDirectoryAName)
        self.__test(1)

    def testTwo(self):
        os.mkdir(self.testSubDirectoryAName)
        os.mkdir(self.testSubDirectoryBName)
        self.__test(2)

    def testNone(self):
        self.assertRaises(TypeError, printFileCount.main, None)

    def testUnknown(self):
        self.assertRaises(
            OSError,
            printFileCount.main,
            '/tmp/thisisaridiculouslylongfilenamethatshouldensureitdoesntactuallyexist')


class PrintFileCountSystemTest(unittest.TestCase):
    def __deleteDirectories(self):
        if os.path.isdir(self.testDirectoryName):
            if os.path.isdir(self.testSubDirectoryAName):
                os.rmdir(self.testSubDirectoryAName)
            if os.path.isdir(self.testSubDirectoryBName):
                os.rmdir(self.testSubDirectoryBName)
            os.rmdir(self.testDirectoryName)

    def setUp(self):
        self.testDirectoryName = '/tmp/russelTest'
        self.testSubDirectoryAName = os.path.join(self.testDirectoryName, 'A')
        self.testSubDirectoryBName = os.path.join(self.testDirectoryName, 'B')
        self.__deleteDirectories()
        os.mkdir(self.testDirectoryName)
        self.cwd = os.getcwd()
        os.chdir(self.testDirectoryName)

    def tearDown(self):
        os.chdir(self.cwd)
        self.__deleteDirectories()

    def __test(self, expected):
        self.assertEqual(expected, int(subprocess.check_output((self.cwd + '/printFileCount.py', self.testDirectoryName)).decode()))

    def testZero(self):
        self.__test(0)

    def testOne(self):
        os.mkdir(self.testSubDirectoryAName)
        self.__test(1)

    def testTwo(self):
        os.mkdir(self.testSubDirectoryAName)
        os.mkdir(self.testSubDirectoryBName)
        self.__test(2)

    def testNone(self):
        self.assertRaises(TypeError, printFileCount.main, None)

    def testUnknown(self):
        self.assertRaises(
            OSError,
            printFileCount.main,
            '/tmp/thisisaridiculouslylongfilenamethatshouldensureitdoesntactuallyexist')


if __name__ == '__main__':
    unittest.main()

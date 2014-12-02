#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A test for the printFileCount_alt script.'''

__author__ = 'Russel Winder'
__date__ = '2012-05-20'
__version__ = '1.2'
__copyright__ = 'Copyright © 2011, 2012  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import unittest
import subprocess
import sys
import os

import printFileCount_alt


class PrintFileCount_Alt_UnitTest(unittest.TestCase):
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

    def __test(self, filesExpected, directoriesExpected):
        self.assertEqual(
            (filesExpected, directoriesExpected),
            printFileCount_alt.getFileAndDirectoryCounts(self.testDirectoryName))

    def testZero(self):
        self.__test(0, 0)

    def testOne(self):
        os.mkdir(self.testSubDirectoryAName)
        self.__test(0, 1)

    def testTwo(self):
        os.mkdir(self.testSubDirectoryAName)
        os.mkdir(self.testSubDirectoryBName)
        self.__test(0, 2)

    def testNone(self):
        self.assertRaises(TypeError, printFileCount_alt.getFileAndDirectoryCounts, None)

    def testUnknown(self):
        self.assertRaises(
            OSError,
            printFileCount_alt.getFileAndDirectoryCounts,
            '/tmp/thisisaridiculouslylongfilenamethatshouldensureitdoesntactuallyexist')


class PrintFileCount_Alt_SystemTest(unittest.TestCase):
    def __deleteDirectories(self):
        if os.path.isdir(self.testDirectoryName):
            if os.path.isdir(self.testSubDirectoryAName):
                os.rmdir(self.testSubDirectoryAName)
            if os.path.isdir(self.testSubDirectoryBName):
                os.rmdir(self.testSubDirectoryBName)
            os.rmdir(self.testDirectoryName)

    def setUp(self):
        self.originalLocation = os.getcwd()
        self.testDirectoryName = '/tmp/russelTest'
        self.testSubDirectoryAName = os.path.join(self.testDirectoryName, 'A')
        self.testSubDirectoryBName = os.path.join(self.testDirectoryName, 'B')
        self.__deleteDirectories()
        os.mkdir(self.testDirectoryName)
        os.chdir(self.testDirectoryName)

    def tearDown(self):
        self.__deleteDirectories()
        os.chdir(self.originalLocation)

    def __test(self, filesExpected, directoriesExpected):
        self.assertEqual(
            'File count = {}, directory count = {}'.format(filesExpected, directoriesExpected),
            subprocess.check_output(os.path.join(self.originalLocation, 'printFileCount_alt.py')).decode().strip())

    def testZero(self):
        self.__test(0, 0)

    def testOne(self):
        os.mkdir(self.testSubDirectoryAName)
        self.__test(0, 1)

    def testTwo(self):
        os.mkdir(self.testSubDirectoryAName)
        os.mkdir(self.testSubDirectoryBName)
        self.__test(0, 2)


if __name__ == '__main__':
    unittest.main()

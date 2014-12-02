#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A test for the script that find files with a .cpp extension.'''

__author__ = 'Russel Winder'
__date__ = '2012-12-01'
__version__ = '1.3'
__copyright__ = 'Copyright © 2007, 2012  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import os.path
import subprocess
import sys
import tempfile
import unittest

import findCodeFiles


class FindCodeFilesUnitTest(unittest.TestCase):
    def testNone(self):
        self.assertRaises(TypeError, findCodeFiles.findCodeFiles, None)

    def testNotList(self):
        self.assertRaises(TypeError, findCodeFiles.findCodeFiles, 0)

    def testFlatDirectoryWithNoEntryStringParameter(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual((), findCodeFiles.findCodeFiles(directory))

    def testFlatDirectoryWithNoEntryTupleParameter(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual((), findCodeFiles.findCodeFiles((directory,)))

    def testFlatDirectoryWithOneEntryPythonStringParameter(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, 'blahblahblah.py')
            with open(path, 'w') as f:
                f.write(' ')
            self.assertEqual((path,), findCodeFiles.findCodeFiles(directory))

    def testFlatDirectoryWithOneEntryPythonTupleParameter(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, 'blahblahblah.py')
            with open(path, 'w') as f:
                f.write(' ')
            self.assertEqual((path,), findCodeFiles.findCodeFiles((directory,)))

    def testFlatDirectoryWithOneEntryNoPythonStringParameter(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, 'blahblahblah')
            with open(path, 'w') as f:
                f.write(' ')
            self.assertEqual((), findCodeFiles.findCodeFiles(directory))

    def testFlatDirectoryWithOneEntryNoPythonTupleParameter(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, 'blahblahblah')
            with open(path, 'w') as f:
                f.write(' ')
            self.assertEqual((), findCodeFiles.findCodeFiles((directory,)))


class FindAllFilesSystemTest(unittest.TestCase):
    scriptName = 'findCodeFiles.py'

    def setUp(self):
        self.workingDirectory = tempfile.TemporaryDirectory()
        self.originalDirectory = os.getcwd()
        os.chdir(self.workingDirectory.name)

    def tearDown(self):
        os.chdir(self.originalDirectory)
        self.workingDirectory.cleanup()

    def testNone(self):
        self.assertEqual('', subprocess.check_output(os.path.join(self.originalDirectory, FindAllFilesSystemTest.scriptName)).decode())

    def testOneEmptyFile(self):
        with tempfile.NamedTemporaryFile(suffix='.py', dir=self.workingDirectory.name) as file:
            self.assertEqual('\t./' + os.path.basename(file.name) + '\n', subprocess.check_output(os.path.join(self.originalDirectory, FindAllFilesSystemTest.scriptName)).decode())


if __name__ == '__main__':
    unittest.main()

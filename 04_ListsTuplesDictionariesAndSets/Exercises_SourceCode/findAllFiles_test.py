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

import findAllFiles


class FindAllFilesUnitTest(unittest.TestCase):
    '''
    Test the findAllFiles.findAllFiles function.
    '''
    def testNone(self):
        self.assertRaises(TypeError, findAllFiles.findAllFiles, None)

    def testNotList(self):
        self.assertRaises(TypeError, findAllFiles.findAllFiles, 0)

    def testFlatDirectoryWithNoEntryStringParameter(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual((), findAllFiles.findAllFiles(directory))

    def testFlatDirectoryWithNoEntryTupleParameter(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual((), findAllFiles.findAllFiles((directory,)))

    def testFlatDirectoryWithOneEntryPythonStringParameter(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, 'blahblahblah.py')
            with open(path, 'w') as f:
                f.write(' ')
            self.assertEqual((('.py', 1),), findAllFiles.findAllFiles(directory))

    def testFlatDirectoryWithOneEntryPythonTupleParameter(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, 'blahblahblah.py')
            with open(path, 'w') as f:
                f.write(' ')
            self.assertEqual((('.py', 1),), findAllFiles.findAllFiles((directory,)))

    def testFlatDirectoryWithOneEntryNoPythonStringParameter(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, 'blahblahblah')
            with open(path, 'w') as f:
                f.write(' ')
            self.assertEqual((('', 1),), findAllFiles.findAllFiles(directory))

    def testFlatDirectoryWithOneEntryNoPythonTupleParameter(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, 'blahblahblah')
            with open(path, 'w') as f:
                f.write(' ')
            self.assertEqual((('', 1),), findAllFiles.findAllFiles((directory,)))


class FindAllFilesSystemTest(unittest.TestCase):
    '''
    Test the findAllFiles.py script.
    '''
    scriptName = 'findAllFiles.py'

    def setUp(self):
        self.workingDirectory = tempfile.TemporaryDirectory()
        self.originalDirectory = os.getcwd()
        os.chdir(self.workingDirectory.name)

    def tearDown(self):
        os.chdir(self.originalDirectory)
        self.workingDirectory.cleanup()

    def testNone(self):
        self.assertEqual('Extension    Count\n', subprocess.check_output(os.path.join(self.originalDirectory, FindAllFilesSystemTest.scriptName)).decode())

    def testOneEmptyFile(self):
        with tempfile.NamedTemporaryFile(suffix='.py', dir=self.workingDirectory.name) as file:
            self.assertEqual('Extension    Count\n  .py	        1\n', subprocess.check_output(os.path.join(self.originalDirectory, FindAllFilesSystemTest.scriptName)).decode())


if __name__ == '__main__':
    unittest.main()

#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A module providing some tests for the option processing script.'''

__author__ = 'Russel Winder'
__date__ = '2014-09-11'
__version__ = '1.1'
__copyright__ = 'Copyright © 2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import sys
import unittest

from docopt import docopt

import optionProcessing_docopt


class CreateParser_Test(unittest.TestCase):
    def testNone(self):
        options = docopt(optionProcessing_docopt.__doc__, ())
        self.assertEqual(0, options['--quiet'])
        self.assertEqual(0, options['--verbose'])

    def testQuietShort(self):
        options = docopt(optionProcessing_docopt.__doc__, ('-q',))
        self.assertEqual(1, options['--quiet'])
        self.assertEqual(0, options['--verbose'])

    def testQuietLong(self):
        options = docopt(optionProcessing_docopt.__doc__, ('--quiet',))
        self.assertEqual(1, options['--quiet'])
        self.assertEqual(0, options['--verbose'])

    def testVerboseShort(self):
        options = docopt(optionProcessing_docopt.__doc__, ('-v',))
        self.assertEqual(0, options['--quiet'])
        self.assertEqual(1, options['--verbose'])

    def testVerboseLong(self):
        options = docopt(optionProcessing_docopt.__doc__, ('--verbose',))
        self.assertEqual(0, options['--quiet'])
        self.assertEqual(1, options['--verbose'])


class ProcessLevel_Test(unittest.TestCase):
    def testDefault(self):
        sys.argv = ['blah']
        self.assertEqual(0, optionProcessing_docopt.processLevel())

    def testThreeVerbose(self):
        sys.argv = ['blah', '-v', '-v', '-v']
        self.assertEqual(3, optionProcessing_docopt.processLevel())

    def testThreeQuiet(self):
        sys.argv = ['blah', '-q', '-q', '-q']
        self.assertEqual(-3, optionProcessing_docopt.processLevel())

    def testVerboseQuietVerbose(self):
        sys.argv = ['blah', '-v', '-q', '-v']
        self.assertEqual(1, optionProcessing_docopt.processLevel())


if __name__ == '__main__':
    unittest.main()

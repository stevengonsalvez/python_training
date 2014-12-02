#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A module providing some tests for the simple option processing script.'''

__author__ = 'Russel Winder'
__date__ = '2014-09-11'
__version__ = '1.3'
__copyright__ = 'Copyright © 2007, 2012–2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import sys
import unittest

from optionProcessing_argparse_simple import createParser, processLevel


class CreateParser_Test(unittest.TestCase):
    def testNone(self):
        options = createParser().parse_args([])
        assert not options.quiet
        assert not options.verbose

    def testQuietShort(self):
        options = createParser().parse_args(['-q'])
        assert options.quiet
        assert not options.verbose

    def testQuietLong(self):
        options = createParser().parse_args(['--quiet'])
        assert options.quiet
        assert not options.verbose

    def testVerboseShort(self):
        options = createParser().parse_args(['-v'])
        assert not options.quiet
        assert options.verbose

    def testVerboseLong(self):
        options = createParser().parse_args(['--verbose'])
        assert not options.quiet
        assert options.verbose


class ProcessLevel_Test(unittest.TestCase):
    def testDefault(self):
        sys.argv = ['blah']
        self.assertEqual(0, processLevel())

    def testThreeVerbose(self):
        sys.argv = ['blah', '-v', '-v', '-v']
        self.assertEqual(1, processLevel())

    def testThreeQuiet(self):
        sys.argv = ['blah', '-q', '-q', '-q']
        self.assertEqual(-1, processLevel())

    def testVerboseQuietVerbose(self):
        sys.argv = ['blah', '-v', '-q', '-v']
        self.assertEqual(1, processLevel())


if __name__ == '__main__':
    unittest.main()

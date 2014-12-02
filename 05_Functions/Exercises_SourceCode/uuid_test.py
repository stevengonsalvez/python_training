#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A module providing tests of the functions from module statistics.'''

__author__ = 'Russel Winder'
__date__ = '2012-09-11'
__version__ = '1.3'
__copyright__ = 'Copyright © 2007,2012 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

from functools import reduce
import operator
import unittest

import uuidGeneration_notUsingUUIDModule
import uuid


class UUIDTests(unittest.TestCase):
    def _checkUUIDString(self, value):
        indexes = (8, 13, 18, 23)

        def report(i):
            return 'index {} failed, was {}'.format(i, value[i])

        for i in range(36):
            if i in indexes:
                assert value[i] == '-', report(i)
            else:
                assert value[i] in '0123456789abcdefABCDEF', report(i)
        assert reduce(
            operator.and_,
            (value[i] == '-' if i in indexes else value[i] in '0123456789abcdefABCDEF'
                for i in range(36)))

    def testUUIDModule(self):
        self._checkUUIDString(str(uuid.uuid4()))

    def testNotUUIDModule(self):
        self._checkUUIDString(uuidGeneration_notUsingUUIDModule.randomUUID())

if __name__ == '__main__':
    unittest.main()

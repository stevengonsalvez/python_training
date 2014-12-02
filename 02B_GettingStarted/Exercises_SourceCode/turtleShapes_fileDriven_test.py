#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''Tests for the shape drawing DSL code.'''

__author__ = 'Russel Winder'
__date__ = '2012-06-25'
__version__ = '1.1'
__copyright__ = 'Copyright © 2012  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import unittest

from turtleShapes_fileDriven import _oneIntegerParameter, _twoIntegerParameters, processCommandLine, dispatcher
from tempfile import NamedTemporaryFile

from unittest.mock import Mock, patch


class OneIntegerParameterFunctionTests(unittest.TestCase):
    def test_int_zero(self):
        self.assertRaises(TypeError, _oneIntegerParameter, 0)

    def test_list_zero(self):
        self.assertRaises(AssertionError, _oneIntegerParameter, [])

    def test_tuple_zero(self):
        self.assertRaises(AssertionError, _oneIntegerParameter, ())

    def test_list_one(self):
        self.assertEqual(1, _oneIntegerParameter(['1']))

    def test_tuple_one(self):
        self.assertEqual(1, _oneIntegerParameter(('1',)))

    def test_list_two(self):
        self.assertRaises(AssertionError, _oneIntegerParameter, ['', ''])

    def test_tuple_two(self):
        self.assertRaises(AssertionError, _oneIntegerParameter, ('', ''))


class TwoIntegerParameterFunctionTests(unittest.TestCase):
    def test_int_zero(self):
        self.assertRaises(TypeError, _twoIntegerParameters, 0)

    def test_list_zero(self):
        self.assertRaises(AssertionError, _twoIntegerParameters, [])

    def test_tuple_zero(self):
        self.assertRaises(AssertionError, _twoIntegerParameters, ())

    def test_list_one(self):
        self.assertRaises(AssertionError, _twoIntegerParameters, [''])

    def test_tuple_one(self):
        self.assertRaises(AssertionError, _twoIntegerParameters, ('',))

    def test_list_two(self):
        self.assertEqual((1, 1), _twoIntegerParameters(['1', '1']))

    def test_tuple_two(self):
        self.assertEqual((1, 1), _twoIntegerParameters(('1', '1')))

    def test_list_three(self):
        self.assertRaises(AssertionError, _twoIntegerParameters, ['', '', ''])

    def test_tuple_three(self):
        self.assertRaises(AssertionError, _twoIntegerParameters, ('', '', ''))


class ProcessCommandLineTest(unittest.TestCase):
    def test_int_zero(self):
        self.assertRaises(TypeError, processCommandLine, 0)

    def test_list_zero(self):
        self.assertRaises(ValueError, processCommandLine, [])

    def test_list_zero(self):
        self.assertRaises(ValueError, processCommandLine, ())

    def test_list_one_invalid(self):
        self.assertRaises(IOError, processCommandLine, [''])

    def test_tuple_one_invalid(self):
        self.assertRaises(IOError, processCommandLine, ('',))

    def test_list_two(self):
        self.assertRaises(ValueError, processCommandLine, ['', ''])

    def test_list_two(self):
        self.assertRaises(ValueError, processCommandLine, ('', ''))

    def test_tuple_one_valid(self):
        with NamedTemporaryFile() as f:
            f.write(bytes('rectangle 10 10', 'utf-8'))
            f.flush()
            f.seek(0)
            mockRectangleFunction = Mock()
            with patch.dict(dispatcher, {'rectangle': mockRectangleFunction}):
                self.assertEqual(None, processCommandLine((f.name,)))
                mockRectangleFunction.assert_called_with(['10', '10'])


if __name__ == '__main__':
    unittest.main()

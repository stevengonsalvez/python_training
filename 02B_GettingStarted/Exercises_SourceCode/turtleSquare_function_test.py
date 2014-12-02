#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''Tests for the shape drawing DSL code.'''

__author__ = 'Russel Winder'
__date__ = '2012-06-25'
__version__ = '1.1'
__copyright__ = 'Copyright © 2012  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

from unittest import TestCase, main
from unittest.mock import patch

import turtle

from turtleSquare_function import drawSquare


class TurtleSquare_Function_Test(TestCase):
    def test_call_with_zero_parameters_raises_exception(self):
        self.assertRaises(TypeError, drawSquare)

    def test_call_with_two_parameters_raises_exception(self):
        self.assertRaises(TypeError, drawSquare, 0, 0)

    def test_call_with_one_parameter_succeeds(self):
        with patch('turtle.forward'), patch('turtle.left'):
            drawSquare(10)
            self.assertEqual(turtle.forward.call_count, 4)
            self.assertEqual(turtle.left.call_count, 3)


if __name__ == '__main__':
    main()

#! /usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Test for the class to represent a matrix including overloads of operators.

This code originally comes from the book "Python for Rookies" by Sarah Mount, James Shuttleworth and Russel
Winder published by Thomson Learning, 2008.
'''

__author__ = 'Russel Winder'
__date__ = '2012-02-18'
__version__ = '1.1'
__copyright__ = 'Copyright © 2007,2012 Russel Winder'
__licence__ = 'GNU General Public Licence (GPL) v3'

import unittest

from matrix import Matrix, zeros, unit


class Matrix_Test(unittest.TestCase):
    def test_Zeros(self):
        xRange = 2
        yRange = 4
        matrix = zeros(xRange, yRange)
        for x in range(xRange):
            for y in range(yRange):
                self.assertEqual(0, matrix[x][y])

    def test_Unit(self):
        xRange = 2
        yRange = 4
        matrix = unit(xRange, yRange)
        for x in range(xRange):
            for y in range(yRange):
                if x == y:
                    self.assertEqual(1, matrix[x][y])
                else:
                    self.assertEqual(0, matrix[x][y])

    def test_AddIntegerTupleCorrect(self):
        # data is a tuple of triplets, the first two are the matrices to be added, the third is the expected
        # answer.
        data = (
            (Matrix(((1, 1), (1, 1))), Matrix(((2, 2), (2, 2))), Matrix(((3, 3), (3, 3)))),
            (Matrix(((1,), (1,), (1,), (1,))), Matrix(((2,), (2,), (2,), (2,))), Matrix(((3,), (3,), (3,), (3,)))),
            (Matrix(((1, 1, 1, 1),)), Matrix(((2, 2, 2, 2),)), Matrix(((3, 3, 3, 3),))))
        for datum in data:
            # Addition should be commutative so try both ways round.
            self.assertEqual(datum[2], datum[0] + datum[1])
            self.assertEqual(datum[2], datum[1] + datum[0])

    def test_AddIntegerListCorrect(self):
        # data is a tuple of triplets, the first two are the matrices to be added, the third is the expected
        # answer.
        data = (
            (Matrix([[1, 1], [1, 1]]), Matrix([[2, 2], [2, 2]]), Matrix([[3, 3], [3, 3]])),
            (Matrix([[1], [1], [1], [1]]), Matrix([[2], [2], [2], [2]]), Matrix([[3], [3], [3], [3]])),
            (Matrix([[1, 1, 1, 1]]), Matrix([[2, 2, 2, 2]]), Matrix([[3, 3, 3, 3]])))
        for datum in data:
            # Addition should be commutative so try both ways round.
            self.assertEqual(datum[2], datum[0] + datum[1])
            self.assertEqual(datum[2], datum[1] + datum[0])

    def test_AddDoubleTupleCorrect(self):
        # data is a tuple of triplets, the first two are the matrices to be added, the third is the expected
        # answer.
        data = (
            (Matrix(((1.0, 1.0), (1.0, 1.0))), Matrix(((2.0, 2.0), (2.0, 2.0))), Matrix(((3.0, 3.0), (3.0, 3.0)))),
            (Matrix(((1.0,), (1.0,), (1.0,), (1.0,))), Matrix(((2.0,), (2.0,), (2.0,), (2.0,))), Matrix(((3.0,), (3.0,), (3.0,), (3.0,)))),
            (Matrix(((1.0, 1.0, 1.0, 1.0),)), Matrix(((2.0, 2.0, 2.0, 2.0),)), Matrix(((3.0, 3.0, 3.0, 3.0),))))
        for datum in data:
            # Addition should be commutative so try both ways round.
            self.assertEqual(datum[2], datum[0] + datum[1])
            self.assertEqual(datum[2], datum[1] + datum[0])

    def test_AddDoubleListCorrect(self):
        # data is a tuple of triplets, the first two are the matrices to be added, the third is the expected
        # answer.
        data = (
            (Matrix([[1.0, 1.0], [1.0, 1.0]]), Matrix([[2.0, 2.0], [2.0, 2.0]]), Matrix([[3.0, 3.0], [3.0, 3.0]])),
            (Matrix([[1.0], [1.0], [1.0], [1.0]]), Matrix([[2.0], [2.0], [2.0], [2.0]]), Matrix([[3.0], [3.0], [3.0], [3.0]])),
            (Matrix([[1.0, 1.0, 1.0, 1.0]]), Matrix([[2.0, 2.0, 2.0, 2.0]]), Matrix([[3.0, 3.0, 3.0, 3.0]])))
        for datum in data:
            # Addition should be commutative so try both ways round.
            self.assertEqual(datum[2], datum[0] + datum[1])
            self.assertEqual(datum[2], datum[1] + datum[0])

    def test_AddIntegerTupleError(self):
        # data is tuple of pairs which should not be addable due to different shapes.
        data = (
            (Matrix(((1, 1), (1, 1))), Matrix(((2,), (2,), (2,), (2,)))),
            (Matrix(((1,), (1,), (1,), (1,))), Matrix(((2, 2, 2, 2),))),
            (Matrix(((1, 1, 1, 1),)), Matrix(((2, 2), (2, 2)))))
        for datum in data:
            self.assertRaises(ValueError, Matrix.__add__, datum[0], datum[1])

    def test_AddIntegerListError(self):
        # data is tuple of pairs which should not be addable due to different shapes.
        data = (
            (Matrix([[1, 1], [1, 1]]), Matrix([[2], [2], [2], [2]])),
            (Matrix([[1], [1], [1], [1]]), Matrix([[2, 2, 2, 2]])),
            (Matrix([[1, 1, 1, 1]]), Matrix([[2, 2], [2, 2]])))
        for datum in data:
            self.assertRaises(ValueError, Matrix.__add__, datum[0], datum[1])

    def test_AddDoubleTupleError(self):
        # data is tuple of pairs which should not be addable due to different shapes.
        data = (
            (Matrix(((1.0, 1.0), (1.0, 1.0))), Matrix(((2.0,), (2.0,), (2.0,), (2.0,)))),
            (Matrix(((1.0,), (1.0,), (1.0,), (1.0,))), Matrix(((2.0, 2.0, 2.0, 2.0),))),
            (Matrix(((1.0, 1.0, 1.0, 1.0),)), Matrix(((2.0, 2.0), (2.0, 2.0)))))
        for datum in data:
            self.assertRaises(ValueError, Matrix.__add__, datum[0], datum[1])

    def test_AddDoubleListError(self):
        # data is tuple of pairs which should not be addable due to different shapes.
        data = (
            (Matrix([[1.0, 1.0], [1.0, 1.0]]), Matrix([[2.0], [2.0], [2.0], [2.0]])),
            (Matrix([[1.0], [1.0], [1.0], [1.0]]), Matrix([[2.0, 2.0, 2.0, 2.0]])),
            (Matrix([[1.0, 1.0, 1.0, 1.0]]), Matrix([[2.0, 2.0], [2.0, 2.0]])))
        for datum in data:
            self.assertRaises(ValueError, Matrix.__add__, datum[0], datum[1])

#  Methods added to answer question are below here ============================

    def test_SubtractCorrect(self):
        data = (
            (Matrix(((1, 1), (1, 1))), Matrix(((2, 2), (2, 2))), Matrix(((-1, -1), (-1, -1)))),
            (Matrix(((1,), (1,), (1,), (1,))), Matrix(((2,), (2,), (2,), (2,))), Matrix(((-1,), (-1,), (-1,), (-1,)))),
            (Matrix(((1, 1, 1, 1),)), Matrix(((2, 2, 2, 2),)), Matrix(((-1, -1, -1, -1),))))
        for datum in data:
            self.assertEqual(datum[2], datum[0] - datum[1])

    def test_SubtractError(self):
        data = (
            (Matrix(((1, 1), (1, 1))), Matrix(((2,), (2,), (2,), (2,)))),
            (Matrix(((1,), (1,), (1,), (1,))), Matrix(((2, 2, 2, 2),))),
            (Matrix(((1, 1, 1, 1),)), Matrix(((2, 2), (2, 2)))))
        for datum in data:
            self.assertRaises(ValueError, Matrix.__sub__, datum[0], datum[1])

    def test_MultiplyCorrect(self):
        data = (
            (Matrix(((1, 1), (1, 1))), Matrix(((2, 2), (2, 2))), Matrix(((4, 4), (4, 4)))),
            (Matrix(((1,), (1,), (1,), (1,))), Matrix(((2, 2, 2, 2),)), Matrix(((2, 2, 2, 2), (2, 2, 2, 2), (2, 2, 2, 2), (2, 2, 2, 2)))),
            (Matrix(((1, 1, 1, 1),)), Matrix(((2,), (2,), (2,), (2,))), Matrix(((8,),))))
        for datum in data:
            self.assertEqual(datum[2], datum[0] * datum[1])

    def test_MultiplyError(self):
        data = (
            (Matrix(((1, 1), (1, 1))), Matrix(((2,), (2,), (2,), (2,)))),
            (Matrix(((1, 1, 1, 1),)), Matrix(((2, 2), (2, 2)))))
        for datum in data:
            self.assertRaises(ValueError, Matrix.__mul__, datum[0], datum[1])

if __name__ == '__main__':
    unittest.main()

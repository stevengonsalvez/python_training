#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''
Class to represent a matrix including overloads of operators.

This code original comes from the book "Python for Rookies" by Sarah Mount, James Shuttleworth and Russel
Winder published by Thomson Learning, 2008.
'''

__author__ = 'Russel Winder'
__date__ = '2012-02-18'
__version__ = '1.1'
__copyright__ = 'Copyright © 2007,2012 Russel Winder'
__licence__ = 'GNU General Public Licence (GPL) v3'


class Matrix:
    def __init__(self, data):
        #  Must do a deep copy of data to avoid any sharing.  Also ensure data is rectangular.
        self.data = []
        columns = len(data[0])
        for row in data:
            if len(row) != columns:
                raise ValueError('Data is not a rectangular structure.')
            self.data += [[x for x in row]]

    def __str__(self):
        result = ''
        for row in self.data:
            result += '| '
            for i in row:
                result += str(i) + ' '
            result += '|\n'
        return result[: len(result) - 1]

# TODO: __repr__

    def __ensureSameShape(self, m):
        if len(self.data) != len(m.data) or len(self.data[0]) != len(m.data[0]):
            raise ValueError('Matrices not of the same shape.')

    def __add__(self, m):
        self.__ensureSameShape(m)
        n = Matrix(self.data)
        for row in range(len(self.data)):
            for column in range(len(self.data[0])):
                n.data[row][column] += m.data[row][column]
        return n

    def __sub__(self, m):
        self.__ensureSameShape(m)
        n = Matrix(self.data)
        for row in range(len(self.data)):
            for column in range(len(self.data[0])):
                n.data[row][column] -= m.data[row][column]
        return n

    def __mul__(self, m):
        if len(self.data[0]) != len(m.data):
            raise ValueError('Matrices not of the suitable shapes for multiplication.')
        n = zeros(len(self.data), len(m.data[0]))
        for row in range(len(n.data)):
            for column in range(len(n.data[0])):
                for i in range(len(self.data[0])):
                    n.data[row][column] += self.data[row][i] * m.data[i][column]
        return n

    def __eq__(self, m):
        try:
            self.__ensureSameShape(m)
        except ValueError:
            return False
        for row in range(len(self.data)):
            for column in range(len(self.data[0])):
                if self.data[row][column] != m.data[row][column]:
                    return False
        return True

#  TODO: __ne__
#  TODO: __hash__

    def __getitem__(self, index):
        '''Deliver a row of the matrix so it can be indexed.'''
        return self.data[index]


def zeros(rows, columns):
    return Matrix([[0.0 for column in range(columns)] for row in range(rows)])


def unit(rows, columns):
    m = Matrix([[0.0 for column in range(columns)] for row in range(rows)])
    for i in range(min(rows, columns)):
        m.data[i][i] = 1.0
    return m

if __name__ == '__main__':
    z = zeros(2, 2)
    u = unit(2, 2)
    assert u == u + z
    assert u == z + u
    assert u == u - z
    a = Matrix(((-1.0, 0.0), (0.0, -1.0)))
    assert a == z - u

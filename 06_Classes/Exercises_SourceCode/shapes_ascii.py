#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A module providing various classes to model shapes being drawn.'''

__author__ = 'Russel Winder'
__date__ = '2012-01-25'
__version__ = '1.1'
__copyright__ = 'Copyright © 2007, 2012  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'


class Shape(object):
    pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return ('*' * self.width + '\n') * self.height


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)


class Triangle(Shape):
    def __init__(self, *args):
        if len(args) == 2:
            self.base = args[0]
            self.height = args[1]
        else:
            raise Exception('Not implemented yet.')

    def __str__(self):
        raise Exception('Not implemented yet.')


class LeftRightangleTriangle(Triangle):
    def __init__(self, base, height):
        Triangle.__init__(self, base, height)

    def __str__(self):
        #  TODO: This needs work!
        putative = '\n'.join('*' * i for i in range(1, self.height + 1))
        return putative + '\n' if putative else ''

if __name__ == '__main__':
    objects = (Rectangle(6, 8), Square(3), LeftRightangleTriangle(3, 4))
    for object in objects:
        print(object)
        print

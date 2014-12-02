#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A module providing various classes to draw shapes using the turtle module.'''

__author__ = 'Russel Winder'
__date__ = '2012-01-26'
__version__ = '1.2'
__copyright__ = 'Copyright © 2007,2012 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import turtle


class Shape(object):
    def draw(self):
        raise Exception('draw method not defined for class: ' + str(type(self)))


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        turtle.forward(self.width)
        turtle.left(90)
        turtle.forward(self.height)
        turtle.left(90)
        turtle.forward(self.width)
        turtle.left(90)
        turtle.forward(self.height)
        turtle.left(90)


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


class LeftRightangleTriangle(Triangle):
    def __init__(self, base, height):
        Triangle.__init__(self, base, height)

    def draw(self):
        x = turtle.xcor()
        y = turtle.ycor()
        turtle.goto(x + self.base, y)
        turtle.goto(x, y + self.height)
        turtle.goto(x, y)

if __name__ == '__main__':
    objects = (Rectangle(60, 80), Square(30), LeftRightangleTriangle(30, 40))
    for object in objects:
        object.draw()
    turtle.exitonclick()

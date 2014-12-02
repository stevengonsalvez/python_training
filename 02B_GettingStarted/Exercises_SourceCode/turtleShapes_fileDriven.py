#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A script that draws shapes as specified in a file.'''

__author__ = 'Russel Winder'
__date__ = '2012-06-25'
__version__ = '1.1'
__copyright__ = 'Copyright © 2011–2012  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import sys
import turtle


def _oneIntegerParameter(x):
    assert len(x) == 1
    return int(x[0])


def _twoIntegerParameters(x):
    assert len(x) == 2
    return(int(x[0]), int(x[1]))


def drawSquare(parameter):
    size = _oneIntegerParameter(parameter)
    turtle.forward(size)
    for i in range(3):
        turtle.left(90)
        turtle.forward(size)


def drawRectangle(parameter):
    height, width = _twoIntegerParameters(parameter)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)


def doMove(parameter):
    turtle.penup()
    turtle.goto(*_twoIntegerParameters(parameter))
    turtle.pendown()


dispatcher = {
    'square': drawSquare,
    'rectangle': drawRectangle,
    'move': doMove}


def processCommandLine(parameter):
    if len(parameter) != 1:
        raise ValueError('One and only one parameter, the name of the file.')
    with open(parameter[0]) as f:
        for l in f:
            # List comprehension used here even though they have not yet been covered in the course at this time.
            item = [i.strip() for i in l.split()]
            dispatcher[item[0]](item[1:])


if __name__ == '__main__':
    processCommandLine(sys.argv[1:])
    turtle.exitonclick()

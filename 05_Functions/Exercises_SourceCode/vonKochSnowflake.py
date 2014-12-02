#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''
A script to draw a von Koch Snowflake using the Turtle package.

This code taken from Mount, Shuttleworth & Winder "Python for Rookies", Thomson Learning and amended to deal
with the changes to the turtle module in Python 2.4 -> Python 2.6 upgrade.
'''

__author__ = 'Russel Winder'
__date__ = '2009-11-27'
__version__ = '1.1'
__copyright__ = 'Copyright © 2007,2009 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import turtle


def initialize(color='brown', smallest=1.0):
    '''Prepare to draw a von Koch Snowflake.'''
    turtle.setup(400, 300)
    turtle.screensize(350, 250)
    turtle.clear()
    turtle.up()
    turtle.goto(-100.0, 55.0)
    turtle.setheading(0)
    turtle.color(color)
    turtle.down()
    global smallestLineLength
    smallestLineLength = smallest


def vonKochCurve(overallLength):
    '''Draw a von Koch Curve of a given length.  The global variable smallestLineLength is assumed to be
    set.'''
    oneThirdLength = overallLength / 3.0
    if oneThirdLength <= smallestLineLength:
        moveFunction = turtle.forward
    else:
        moveFunction = vonKochCurve
    moveFunction(oneThirdLength)
    turtle.left(60)
    moveFunction(oneThirdLength)
    turtle.right(120)
    moveFunction(oneThirdLength)
    turtle.left(60)
    moveFunction(oneThirdLength)


def vonKochSnowflake(overall, smallest=1.0, color='blue'):
    '''Generate a von Koch Snowflake (which is a triangle of von Koch Curves).'''
    initialize(color, smallest)
    vonKochCurve(overall)
    turtle.right(120)
    vonKochCurve(overall)
    turtle.right(120)
    vonKochCurve(overall)


if __name__ == '__main__':
    #turtle.speed(1)
    vonKochSnowflake(200.0, 2.0)
    turtle.exitonclick()

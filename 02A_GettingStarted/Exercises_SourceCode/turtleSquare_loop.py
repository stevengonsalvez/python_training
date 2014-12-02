#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A script that draws a square of size 100 using turtle graphics.'''

__author__ = 'Russel Winder'
__date__ = '2012-02-18'
__version__ = '1.1'
__copyright__ = 'Copyright © 2011–2012  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import turtle

if __name__ == '__main__':
    turtle.forward(100)
    for i in range(3):
        turtle.left(90)
        turtle.forward(100)

    #input('Waiting for input to retain display...')
    turtle.exitonclick()

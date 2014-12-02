#! /usr/bin/env py.test-3
# -*- coding:utf-8; -*-

'''A module providing a test for future value module.'''

__author__ = 'Russel Winder'
__date__ = '2014-06-30'
__version__ = '1.0'
__copyright__ = 'Copyright © 2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import pytest
import subprocess

from interestingAmount import FV

data = (
    (100, 0.03, 10, 134.39),
    (100, 0.05, 10, 162.89),
    (100, 0.07, 10, 196.72),
)


@pytest.mark.parametrize(('principal', 'rate', 'period', 'value'), data)
def testFVSuccess(principal, rate, period, value):
    assert abs(value - FV(principal, rate, period)) < 0.01


def test_script_hundred():
    expected = '''  1 103.00 105.00 107.00
  2 106.09 110.25 114.49
  3 109.27 115.76 122.50
  4 112.55 121.55 131.08
  5 115.93 127.63 140.26
  6 119.41 134.01 150.07
  7 122.99 140.71 160.58
  8 126.68 147.75 171.82
  9 130.48 155.13 183.85
 10 134.39 162.89 196.72
'''.splitlines()
    assert expected == subprocess.check_output(('python3', 'interestingAmount.py', '100')).decode().splitlines()


def test_script_too_few_arguments():
    assert 1 == subprocess.call(('python3', 'interestingAmount.py'))


def test_script_too_many_arguments():
    assert 1 == subprocess.call(('python3', 'interestingAmount.py', '100', '10'))

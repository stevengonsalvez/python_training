#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''Test for the various functions for generating permutations.'''

__author__ = 'Russel Winder'
__date__ = '2014-09-27'
__version__ = '1.4'
__copyright__ = 'Copyright © 2007, 2012, 2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

from functools import wraps
import unittest

import permutations


class PermutationsTest(unittest.TestCase):

    #  Comparing two sequences for having the same members can be handled as a pair of iterations to
    #  test that all members of one sequence are members of the other, or by creating sets and checking
    #  set equality. The latter seems simpler. Only hashable values can go into sets though, so we
    #  cannot test sequences of lists that way – at least not directly. Hence this function.
    def __assert_two_sequences_of_lists_equal(self, a, b):
        tA = {tuple(x) for x in a}
        tB = {tuple(x) for x in b}
        self.assertEqual(tA, tB)

    def __check_empty_list(self, function):
        iterator = iter(function([]))
        self.assertEqual([], next(iterator))
        self.assertRaises(StopIteration, iterator.__next__)

    def __check_single_item_list(self, function):
        iterator = iter(function(['a']))
        self.assertEqual(['a'], next(iterator))
        self.assertRaises(StopIteration, iterator.__next__)

    def __check_two_item_list(self, function):
        iterator = iter(function('ab'))
        self.__assert_two_sequences_of_lists_equal((['a', 'b'], ['b', 'a']), [next(iterator) for i in range(2)])
        self.assertRaises(StopIteration, iterator.__next__)

    def __check_three_item_list(self, function):
        iterator = iter(function(['a', 'b', 'c']))
        self.__assert_two_sequences_of_lists_equal((['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'a', 'c'], ['b', 'c', 'a'], ['c', 'a', 'b'], ['c', 'b', 'a']), [next(iterator) for i in range(6)])
        self.assertRaises(StopIteration, iterator.__next__)

    def __check_empty_string(self, function):
        iterator = iter(function(''))
        self.assertEqual('', next(iterator))
        self.assertRaises(StopIteration, iterator.__next__)

    def __check_single_item_string(self, function):
        iterator = iter(function('a'))
        self.assertEqual('a', next(iterator))
        self.assertRaises(StopIteration, iterator.__next__)

    def __check_two_item_string(self, function):
        iterator = iter(function('ab'))
        self.assertEqual(set(('ab', 'ba')), {next(iterator) for i in range(2)})
        self.assertRaises(StopIteration, iterator.__next__)

    def __check_three_item_string(self, function):
        iterator = iter(function('abc'))
        self.assertEqual(set(('abc', 'acb', 'bac', 'bca', 'cab', 'cba')), {next(iterator) for i in range(6)})
        self.assertRaises(StopIteration, iterator.__next__)


def _inject_test(test, function):
    @wraps(function)
    def f(self, test=test, function=function):
        PermutationsTest.__dict__[test](self, function)
    setattr(PermutationsTest, 'test__' + test + '__' + f.__name__, f)


# Must capture the whole list of current items immediately. If we do not then the iteration fails because we
# add new entries into the dictionary.
for test_name in tuple(x for x in PermutationsTest.__dict__ if '__check_' in x):
    for function_reference in (
        permutations.permutations_iteration,
        permutations.permutations_comprehension,
        permutations.permutations_comprehension_alt,
        permutations.permutations_generator,
    ):
        _inject_test(test_name, function_reference)

if __name__ == '__main__':
    unittest.main()

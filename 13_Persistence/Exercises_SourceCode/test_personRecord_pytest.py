#! /usr/bin/env py.test-3

'''
A class instances of which represent data records for people. This is intended to be a value type.
'''

__author__ = 'Russel Winder'
__date__ = '2014-07-23'
__version__ = '1.3'
__copyright__ = 'Copyright © 2010–2012, 2014 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

from unittest import TestCase, main

from personRecord import PersonRecord

datum = ('Winder', 'Russel', '41 Buckmaster Road, London SW11 1EN', '020 7585 2200', '07770 465 077')


def test_empty_record_repr():
    assert 'PersonRecord("","","","","")' == repr(PersonRecord())


def test_single_full_record_repr():
    assert 'PersonRecord("{}","{}","{}","{}","{}")'.format(*datum) == repr(PersonRecord(* datum))


def test_empty_record_as_tuple():
    assert ('', '', '', '', '') == PersonRecord().asTuple()


def test_single_full_record_as_tuple():
    assert datum == PersonRecord(* datum).asTuple()


def test_value_equality_empty_records():
    assert PersonRecord() == PersonRecord()


def test_value_inequality_partial_records():
    assert PersonRecord('Winder') != PersonRecord('Bloggs')


def test_value_inequality_fails_on_empty_records():
    assert not(PersonRecord() != PersonRecord())


def test_value_inequality_fails_on_partial_records():
    assert not(PersonRecord('Winder') != PersonRecord('Winder'))

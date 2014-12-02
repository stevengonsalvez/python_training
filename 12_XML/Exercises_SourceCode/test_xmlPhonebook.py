#! /usr/bin/env py.test-3

'''
Tests for the module realizing the XML storage using lxml.
'''

__author__ = 'Russel Winder'
__version__ = '1.2'
__date__ = '2014-08-23'
__copyright__ = 'Copyright © 2007, 2012. 2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import tempfile
import sys
from lxml.etree import ParseError

from xmlPhonebook import Context

emptyContactsDocument = '<contacts xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="contacts.xsd"></contacts>'
basicContactsDocument = '''<contacts xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="contacts.xsd">
  <contact>
    <name>
      <firstname>Russel</firstname>
      <lastname>Winder</lastname>
    </name>
    <number>+44 20 7585 2200</number>
  </contact>
</contacts>
'''
basicKey = 'Winder, Russel'
basicValue = '+44 20 7585 2200'


def _setUp_empty(f):
    f.write(emptyContactsDocument.encode())
    f.seek(0)


def _setUp_basic(f):
    f.write(basicContactsDocument.encode())
    f.seek(0)


def test_non_existent_file():
    try:
        Context('thisfilenameissoridiculousthatitcantpossiblyactualyexistonthefilestore')
        self.fail('Did not raise IOError.')
    except IOError:
        pass


def test_empty_file():
    with tempfile.NamedTemporaryFile() as f:
        try:
            Context(f.name)
            self.fail('Did not raise ParseError.')
        except ParseError:
            pass


def test_wellFormed_but_contactless_file_default():
    with tempfile.NamedTemporaryFile() as f:
        _setUp_empty(f)
        context = Context(f.name)
        assert (context.filename, context.mode, context.writebackOnExit, context.cache) == (f.name, 'r+b', True, {})


def test_wellFormed_but_contactless_file_no_writeback():
    with tempfile.NamedTemporaryFile() as f:
        _setUp_empty(f)
        context = Context(f.name, 'r', False)
        assert (context.filename, context.mode, context.writebackOnExit, context.cache) == (f.name, 'r', False, {})


def test_file_with_one_entry():
    with tempfile.NamedTemporaryFile() as f:
        _setUp_basic(f)
        context = Context(f.name)
        assert (context.filename, context.mode, context.writebackOnExit, context.cache) == (f.name, 'r+b', True, {basicKey: basicValue})


def test_reasonable_output_from_an_entry():
    with tempfile.NamedTemporaryFile() as f:
        _setUp_empty(f)
        with Context(f.name) as context:
            assert (context.filename, context.mode, context.writebackOnExit, context.cache) == (f.name, 'r+b', True, {})
            context.cache = {basicKey: basicValue}
        assert basicContactsDocument == f.read().decode()


def test_can_get_an_item_from_cache():
    with tempfile.NamedTemporaryFile() as f:
        _setUp_basic(f)
        context = Context(f.name)
        assert context[basicKey] == basicValue


def test_can_set_an_item_to_an_empty_cache():
    with tempfile.NamedTemporaryFile() as f:
        _setUp_empty(f)
        context = Context(f.name)
        context[basicKey] = basicValue
        assert context[basicKey] == basicValue


def test_use_context_manager_in_with_statement():
    with tempfile.NamedTemporaryFile() as f:
        _setUp_basic(f)
        with Context(f.name) as contacts:
            assert contacts[basicKey] == basicValue


def test_keys_method_delivers_keys():
    with tempfile.NamedTemporaryFile() as f:
        _setUp_basic(f)
        with Context(f.name) as contacts:
            assert contacts.keys() == {basicKey: ''}.keys()

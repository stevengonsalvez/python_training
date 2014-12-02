'''
A module using lxml to realize storing phone book data stored as an XML
file on disc.  Implement as a context manager so as to be usable with
the with statement and hence ensure write-back of the current in all
cases if any writeback is desired.
'''

__author__ = 'Russel Winder'
__version__ = '1.1'
__date__ = '2014-08-23'
__copyright__ = 'Copyright © 2007, 2012, 2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import sys
from lxml.etree import XMLParser, XMLSchema, parse, tostring
from lxml.builder import E


class Context(object):
    '''
    A context manager that looks a bit like a dictionary to act as an
    adapter between applications wanting to work with a dictionary-like
    data structure and something that reads an XML file from disc to
    initialize the dictionary like object and then writes the new XML
    file to disc when the docition is finished with.
    '''
    def __init__(self, filename, mode='r+b', writebackOnExit=True):
        '''
        Creating a phonebook context manager requires a filename; opening mode
        and whether there is write back on exit are optional arguments.
        If write back on exit is True then there must be a mode which
        allows for writing. The mode must always allow reading!
        '''
        self.filename = filename
        self.mode = mode
        self.writebackOnExit = writebackOnExit
        # TODO: Validate the document.
        parser = XMLParser(schema=XMLSchema(parse('contacts.xsd')))
        self.cache = {
            item.find('name/lastname').text + ', ' + item.find('name/firstname').text: item.find('number').text
            for item in parse(filename, parser).findall('contact')}

    def __enter__(self):
        return self

    def __exit__(self, e_type, e_value, e_traceback):
        if self.writebackOnExit:
            contacts = []
            for key, value in self.cache.items():
                l_name, f_name = [s.strip() for s in key.split(',')]
                contacts.append(E.contact(E.name(E.firstname(f_name), E.lastname(l_name)), E.number(value)))
            contacts.append({'{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation': 'contacts.xsd'})
            contacts = E.contacts(*contacts)
            with open(self.filename, 'wb') as f:
                f.write(tostring(contacts, pretty_print=True))
        return e_type is None

    def __getitem__(self, key):
        return self.cache[key]

    def __setitem__(self, key, value):
        self.cache[key] = value

    def keys(self):
        return self.cache.keys()

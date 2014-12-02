#! /usr/bin/env python3

# PyMongo not available for Python 3 on Debian Unstable.

'''
Contacts database realized using PyMongo.
'''

__author__ = 'Russel Winder'
__date__ = '2012-08-20'
__version__ = '1.2'
__copyright__ = 'Copyright © 2010–2012 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import pymongo

from personRecord import PersonRecord


class Connection(object):
    '''
    Contacts database oriented class for managing connections to a MongoDB database.  An instance of this
    class opens a connection to a database which must be closed. Instances are context managers and can be
    used in with statements.
    '''
    def __init__(self, url):
        self.connection = pymongo.Connection(* url) if url else pymongo.Connection()
        self.contacts = self.connection.contactsDB.contacts

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        '''
        Close the open connection to the database.
        '''
        self.connection.disconnect()

    def initializeDatabase(self):
        '''
        Initialize the database. Just drop all previous data.
        '''
        self.contacts.drop()

    def addEntry(self, datum):
        '''
        Add a new record into the database.
        '''
        assert isinstance(datum, PersonRecord)
        self.contacts.insert({(datum.lastname, datum.firstname): datum})

    def getEntry(self, datum):
        '''
        Return one or more entries by providing a selector in terms of a sequence with column entries. An
        empty string means no selector.
        '''
        returnValue = None
        return returnValue

    def deleteEntry(self, datum):
        '''
        Delete one or more entries by providing a selector in terms of a sequence with column entries. An empty
        string means no selector.
        '''
        pass

    def getAllEntries(self):
        '''
        Return a tuple of all the records from the database, including all columns.
        '''
        return tuple([r for r in self.contacts.find()])

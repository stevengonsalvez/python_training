#! /usr/bin/env python3

'''
Contacts database realized using SQLAlchemy using the "hybrid" mode of working.
'''

__author__ = 'Russel Winder'
__date__ = '2012-08-20'
__version__ = '1.2'
__copyright__ = 'Copyright © 2010–2012 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

from sqlalchemy import Table, Column, Unicode, MetaData
from sqlalchemy.orm import mapper, sessionmaker
from os import remove

from personRecord import PersonRecord


def tableStructure(metaData):
    return Table(
        'recordTable', metaData,
        Column('lastname', Unicode(30)),
        Column('firstname', Unicode(30), primary_key=True),
        Column('address', Unicode(90)),
        Column('landline', Unicode(15)),
        Column('mobile', Unicode(15)))


class Connection:
    '''
    Contacts database oriented class for managing connections to a database.  An instance of this class
    opens a connection to a database which must be closed. Instances are context managers and can be used in
    with statements.
    '''
    def __init__(self, url):
        self.metaData = MetaData(url)
        mapper(PersonRecord, tableStructure(self.metaData))
        self.session = sessionmaker()()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        '''
        Close the open connection to the database.
        '''
        clear_mappers()

    def initializeDatabase(self):
        '''
        Initialize the database with the columns required to store the contacts database records.
        '''
        self.metaData.create_all()

    def addEntry(self, datum):
        '''
        Add a new record into the database. The second parameter is a sequence with entries for each column.
        '''
        self.session.add(PersonRecord(datum))

    def getEntry(self, datum):
        '''
        Return one or more entries by providing a selector in terms of a sequence with column entries. An
        empty string means no selector.
        '''
        assert 0 < len(datum) <= 5
        returnValue = None
        return returnValue

    def deleteEntry(self, datum):
        '''
        Delete one or more entries by providing a selector in terms of a sequence with column entries. An empty
        string means no selector.
        '''
        assert 0 < len(datum) <= 5

    def getAllEntries(self):
        '''
        Return a tuple of all the records from the database, including all columns.
        '''
        return [r for r in self.session.query(PersonRecord)]

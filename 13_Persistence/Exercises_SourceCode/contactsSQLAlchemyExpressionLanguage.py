#! /usr/bin/env python3

'''
Contacts database realized using SQLAlchemy using the "expression language" mode of working.
'''

__author__ = 'Russel Winder'
__date__ = '2012-08-20'
__version__ = '1.2'
__copyright__ = 'Copyright © 2010–2012 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

from sqlalchemy import Table, Column, Unicode, MetaData, create_engine
from os import remove

from personRecord import PersonRecord


def tableStructure(metaData):
    return Table(
        'recordTable', metaData,
        Column('lastname', Unicode(30)),
        Column('firstname', Unicode(30)),
        Column('address', Unicode(90)),
        Column('landline', Unicode(15)),
        Column('mobile', Unicode(15)))


class Connection:
    '''
    Contacts database oriented class for managing connections to a SQLite3 database.  An instance of this
    class opens a connection to a database which must be closed. Instances are context managers and can be
    used in with statements.
    '''
    def __init__(self, url):
        self.engine = create_engine(url, echo=True)
        self.metaData = MetaData()
        self.recordTable = tableStructure(self.metaData)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        '''
        Close the open connection to the database.
        '''
        pass

    def initializeDatabase(self):
        '''
        Initialize the database with the columns required to store the contacts database records.
        '''
        self.metaData.create_all(self.engine)

    def getAllEntries(self):
        '''
        Return one or more entries by providing a selector in terms of a sequence with column entries. An
        empty string means no selector.
        '''
        return [PersonRecord(*r) for r in self.recordTable.select().execute()]

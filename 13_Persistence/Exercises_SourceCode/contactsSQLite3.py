#! /usr/bin/env python3

'''
Contacts database realized using SQLite3
'''

__author__ = 'Russel Winder'
__date__ = '2012-08-20'
__version__ = '1.2'
__copyright__ = 'Copyright © 2010–2012 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import sqlite3

from contextlib import closing

from personRecord import PersonRecord

columnNames = ('lastname', 'firstname', 'address', 'landline', 'mobile')


class Connection:
    '''
    Contacts database oriented class for managing connections to a SQLite3 database.  An instance of this
    class opens a connection to a database which must be closed. Instances are context managers and can be
    used in with statements.
    '''
    def __init__(self, databaseName):
        self.connection = sqlite3.connect(databaseName)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        '''
        Close the open connection to the database.
        '''
        self.connection.close()

    def initializeDatabase(self):
        '''
        Initialize the database with the columns required to store the contacts database records.
        '''
        with self.connection, closing(self.connection.cursor()) as cursor:
            cursor.execute('create table contacts({})'.format(','.join(columnName + ' text' for columnName in columnNames)))

    def addEntry(self, datum):
        '''
        Add a new record into the database. The second parameter is a sequence with entries for each column.
        '''
        assert isinstance(datum, PersonRecord)
        with self.connection, closing(self.connection.cursor()) as cursor:
                cursor.execute('insert into contacts values("{}", "{}", "{}", "{}", "{}")'.format(* datum.asTuple()))

    def getEntry(self, datum):
        '''
        Return one or more entries by providing a selector in terms of a sequence with column entries. An
        empty string means no selector.
        '''
        datum = datum.asTuple()
        assert len(datum) == 5
        whereClause = ''
        if datum[0] != '':
            whereClause += 'where {} = "{}"'.format(columnNames[0], datum[0])
        for i in range(1, len(datum)):
            if datum[i] != '':
                whereClause += ('where' if len(whereClause) == 0 else 'and') + ' {} = "{}"'.format(columnNames[i], datum[i])
        assert whereClause[0:5] == 'where'
        returnValue = None
        with self.connection, closing(self.connection.cursor()) as cursor:
            cursor.execute('select * from contacts ' + whereClause)
            returnValue = tuple([PersonRecord(* columns) for columns in cursor])
        return returnValue

    def deleteEntry(self, datum):
        '''
        Delete one or more entries by providing a selector in terms of a sequence with column entries. An empty
        string means no selector.
        '''
        datum = datum.asTuple()
        assert len(datum) == 5
        whereClause = ''
        if datum[0] != '':
            whereClause += 'where {} = "{}"'.format(columnNames[0], datum[0])
        for i in range(1, len(datum)):
            if datum[i] != '':
                whereClause += ('where' if len(whereClause) == 0 else 'and') + ' {} = "{}"'.format(columnNames[i], datum[i])
        assert whereClause[0:5] == 'where'
        with self.connection, closing(self.connection.cursor()) as cursor:
            cursor.execute('delete from contacts ' + whereClause)

    def getAllEntries(self):
        '''
        Return a tuple of all the records from the database, including all columns.
        '''
        returnValue = None
        with self.connection, closing(self.connection.cursor()) as cursor:
            cursor.execute('select * from contacts')
            returnValue = tuple([PersonRecord(* columns) for columns in cursor])
        return returnValue

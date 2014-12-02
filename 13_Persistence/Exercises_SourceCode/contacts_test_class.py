#! /usr/bin/env python3

'''
A module providing a test class that tests the API independent of the actual underlying database,
'''

__author__ = 'Russel Winder'
__date__ = '2012-08-20'
__version__ = '1.2'
__copyright__ = 'Copyright © 2010–2012 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

from personRecord import PersonRecord

from unittest import TestCase

# These values will be set by the importing code. It's effectively dependency injection so that features
# used here are provided by the importing module.

url = None
ConnectionClass = None


class TestContacts(TestCase):
    '''
    This is an integration test for a Connection class. The functions are not easily amenable to unit
    testing using mocks. The point here is that we want more functionality/requirements-oriented testing
    rather than implementation-oriented testing. This is more behaviour-driven rather than test-driven.

    There is an assumption of the existence of a getConnectionInstance function returning a connection
    instance.
    '''
    personA = PersonRecord('Winder', 'Russel', '41 Buckmaster Road, London SW11 1EN', '020 7585 2200', '07770 465 077')
    personB = PersonRecord('Winder', 'Geri', '41 Buckmaster Road, London SW11 1EN', '020 7585 2200', '')

    def setUp(self):
        # Since each test is self-contained, indeed there must not be any data coupling between tests, we
        # can use an in-memory SQLite3 database, thereby speeding up the tests.
        self.connection = ConnectionClass(url)
        self.connection.initializeDatabase()

    def tearDown(self):
        self.connection.close()

    def test_emptyDatabaseHasNoEntries(self):
        self.assertEqual((), self.connection.getAllEntries())

    def test_addOnePerson(self):
        self.connection.addEntry(TestContacts.personA)
        self.assertEqual((TestContacts.personA,), self.connection.getAllEntries())

    def test_addTwoPeople(self):
        self.connection.addEntry(TestContacts.personA)
        self.connection.addEntry(TestContacts.personB)
        self.assertEqual((TestContacts.personA, TestContacts.personB), self.connection.getAllEntries())

    def test_addOnePersonAndRemoveThemByLastname(self):
        self.connection.addEntry(TestContacts.personA)
        self.connection.deleteEntry(PersonRecord(TestContacts.personA.lastname,))
        self.assertEqual((), self.connection.getAllEntries())

    def test_addOnePersonAndRemoveThemByFirstname(self):
        self.connection.addEntry(TestContacts.personA)
        self.connection.deleteEntry(PersonRecord('', TestContacts.personA.firstname))
        self.assertEqual((), self.connection.getAllEntries())

    def test_addOnePersonAndRemoveThemByLastnameAndFirstname(self):
        self.connection.addEntry(TestContacts.personA)
        self.connection.deleteEntry(PersonRecord(TestContacts.personA.lastname, TestContacts.personA.firstname))
        self.assertEqual((), self.connection.getAllEntries())

    def test_addTwoPeopleAndGetByLastname(self):
        self.connection.addEntry(TestContacts.personA)
        self.connection.addEntry(TestContacts.personB)
        self.assertEqual((TestContacts.personA, TestContacts.personB), self.connection.getEntry(PersonRecord('Winder',)))

    def test_addTwoPeopleAndGetByFirstname(self):
        self.connection.addEntry(TestContacts.personA)
        self.connection.addEntry(TestContacts.personB)
        self.assertEqual((TestContacts.personA,), self.connection.getEntry(PersonRecord('', 'Russel')))

    def test_addTwoPeopleAndGetByLastnameAndFirstname(self):
        self.connection.addEntry(TestContacts.personA)
        self.connection.addEntry(TestContacts.personB)
        self.assertEqual((TestContacts.personA,), self.connection.getEntry(PersonRecord('Winder', 'Russel')))

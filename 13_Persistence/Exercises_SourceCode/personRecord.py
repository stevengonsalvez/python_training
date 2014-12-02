#! /usr/bin/env python3

'''
A class instances of which represent data records for people. This is intended to be a value type.
'''

__author__ = 'Russel Winder'
__date__ = '2012-08-20'
__version__ = '1.2'
__copyright__ = 'Copyright © 2010–2012 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'


class PersonRecord(object):
    def __init__(self, *args):
        self.lastname, self.firstname, self.address, self.landline, self.mobile = tuple([args[i] if i < len(args) else '' for i in range(5)])

    def __eq__(self, other):
        return self.lastname == other.lastname and \
            self.firstname == other.firstname and \
            self.address == other.address and \
            self.landline == other.landline and \
            self.mobile == other.mobile

    def __ne__(self, other):
        return not(self == other)

    def __hash__(self):
        return hash((self.lastname, self.firstname, self.address, self.landline, self.mobile))

    def __repr__(self):
        # TODO: Need to escape,
        return 'PersonRecord("{}","{}","{}","{}","{}")'.format(self.lastname, self.firstname, self.address, self.landline, self.mobile)

    def asTuple(self):
        '''
        Return a tuple of the values of the record:

           (lastname, firstname, address, landline, mobile)
        '''
        return(self.lastname, self.firstname, self.address, self.landline, self.mobile)

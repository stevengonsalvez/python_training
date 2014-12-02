#! /usr/bin/env python3
# -*- coding:utf-8; -*-

#  This is a model of the "The Sleeping Barber" problem using Python (http://www.python.org) and PyCSP
#  (http://code.google.com/p/pycsp/), cf. http://en.wikipedia.org/wiki/Sleeping_barber_problem.
#
#  Copyright © 2009–2012 Russel Winder

#  The barber's shop and the barber are modelled with processes.  Channels are used to pass customer objects
#  from the shop to the barber.  The current arrangement assumes there is only one barber.

#  This should work with both Python 2 and Python 3.  Use range everywhere, even where with Python 2 xrange
#  would be preferred so as to ensure it all works with both versions.

import time
import random

from pycsp.processes import (process, retire, poison, Channel, Parallel, AltSelect,
                              InputGuard, OutputGuard, TimeoutGuard, ChannelPoisonException)

class Customer(object):
    def __init__(self, id):
        self.id = id

@process
def barber(identity, hairTrimTime, fromShopIn, toShopOut):
    def _message(message):
        print ('Barber ' + str(identity) + ': ' + str(message))
    while True:
        customer = fromShopIn()
        assert isinstance(customer, Customer)
        _message('Barber: Starting Customer ' + str(customer.id))
        time.sleep(hairTrimTime())
        _message('Barber: Finished Customer ' + str(customer.id))
        toShopOut(customer)

@process
def shopIn(numberOfWaitingSeats, fromWorld, toBarber, toAccounts):
    seats = []

    def trySendingToBarber(customer):
        channel, message = AltSelect(OutputGuard(toBarber, msg=seats[0]), TimeoutGuard(seconds=0.1))
        if channel == toBarber:
            del customer
    try:
        while True:
            customer = fromWorld()
            assert isinstance(customer, Customer)
            if len(seats) < numberOfWaitingSeats:
                seats.append(customer)
                print('Shop: Customer ' + str(customer.id) + ' takes a seat. ' + str(len(seats)) + ' in use.')
                channel, message = AltSelect(OutputGuard(toBarber, msg=seats[0]), TimeoutGuard(seconds=0.1))
                if channel == toBarber:
                    seats = seats[1:]
            else:
                if len(seats) > 0:
                    channel, message = AltSelect(OutputGuard(toBarber, msg=seats[0]), TimeoutGuard(seconds=0.1))
                    if channel == toBarber:
                        seats = seats[1:]
                print('Shop: Customer ' + str(customer.id) + ' turned away.')
                toAccounts(customer)
    except ChannelPoisonException:
        while(len(seats) > 0):
            toBarber(seats[0])
            seats = seats[1:]
        poison(toBarber)

@process
def shopOut(fromBarber, toAccounts):
    while True:
        customer = fromBarber()
        assert isinstance(customer, Customer)
        print('Shop: Customer ' + str(customer.id) + ' leaving trimmed.')
        toAccounts(customer)

@process
def accounts(fromShopIn, fromShopOut):
    customersTurnedAway = 0
    customersTrimmed = 0
    try:
        while True:
            channel, customer = AltSelect(InputGuard(fromShopIn), InputGuard(fromShopOut))
            if channel == fromShopIn:
                customersTurnedAway += 1
            elif channel == fromShopOut:
                customersTrimmed += 1
            else:
                raise ValueError('Incorrect return from AltSelect.')
    except ChannelPoisonException:
        print('\nTrimmed ' + str(customersTrimmed) + ' and turnedAway ' + str(customersTurnedAway) + ' today.')

@process
def world(numberOfCustomers, nextCustomerWaitTime, toShopIn):
    for i in range(numberOfCustomers):
        time.sleep(nextCustomerWaitTime())
        toShopIn(Customer(i))
    poison(toShopIn)

def main(numberOfCustomers, numberOfWaitingSeats, numberOfBarbers, nextCustomerWaitTime, hairTrimTime):
    worldToShopIn = Channel()
    shopOutToShopIn = Channel()
    toBarber = Channel()
    toShopOut = Channel()
    shopInToAccounts = Channel()
    shopOutToAccounts = Channel()
    Parallel(
        shopIn(numberOfWaitingSeats, worldToShopIn.reader(), toBarber.writer(), shopInToAccounts.writer()),
        shopOut(toShopOut.reader(), shopOutToAccounts.writer()),
        accounts(shopInToAccounts.reader(), shopOutToAccounts.reader()),
        world(numberOfCustomers, nextCustomerWaitTime, worldToShopIn.writer()),
        *[barber(i, hairTrimTime, toBarber.reader(), toShopOut.writer()) for i in range(numberOfBarbers)]
       )

if __name__ == '__main__':
    main(1000, 8, 4,  lambda: random.random() * 0.002 + 0.001, lambda: random.random() * 0.008 + 0.001)

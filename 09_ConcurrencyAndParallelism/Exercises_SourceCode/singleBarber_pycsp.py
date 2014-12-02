#! /usr/bin/env python3
# -*- coding:utf-8; -*-

#  This is a model of the "The Sleeping Barber" problem using Python and PyCSP
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

class SuccessfulCustomer(object):
    def __init__(self, customer):
        self.c = customer

@process
def barber(hairTrimTime, fromShop, toShop):
    customersTrimmed = 0
    try:
        while True:
            customer = fromShop()
            assert isinstance(customer, Customer)
            print('Barber: Starting Customer ' + str(customer.id))
            time.sleep(hairTrimTime())
            customersTrimmed += 1
            print('Barber: Finished Customer ' + str(customer.id))
            toShop(SuccessfulCustomer(customer))
    except ChannelPoisonException:
        print('Barber: Clocking off, trimmed ' + str(customersTrimmed) + ' today.')

@process
def shop(numberOfWaitingSeats, fromWorld, toBarber, fromBarber, toWorld):
    seats = []
    customersTrimmed = 0
    customersTurnedAway = 0
    closing = False
    while True:
        try:
            if closing:
                channel, customer = fromBarber, fromBarber()
            else:
                # Order of channels is important here as it defines the priority of the channels.
                channel, customer = AltSelect(InputGuard(fromBarber), InputGuard(fromWorld))
            if channel == fromWorld:
                assert isinstance(customer, Customer)
                if len(seats) <= numberOfWaitingSeats:
                    seats.append(customer)
                    print('Shop: Customer ' + str(customer.id) + ' takes a seat. ' + str(len(seats)) + ' in use.')
                else:
                    print('Shop: Customer ' + str(customer.id) + ' turned away.')
                    customersTurnedAway += 1
                    toWorld(customer)
            elif channel == fromBarber:
                assert isinstance(customer, SuccessfulCustomer)
                print('Shop: Customer ' + str(customer.c.id) + ' leaving trimmed.')
                customersTrimmed += 1
                toWorld(customer)
            else:
                raise ValueError('Shop: AltSelect failed.')
            if len(seats) > 0:
                channel, message = AltSelect(OutputGuard(toBarber, msg=seats[0]), TimeoutGuard(seconds=0.1))
                if channel == toBarber:
                    del(seats[0])
            else:
                if closing:
                    poison(toBarber)
                    print('Shop: Closing -- ' + str(customersTrimmed) + ' trimmed, and ' + str(customersTurnedAway) + ' turned away.')
                    poison(toWorld)
                    break
        except ChannelPoisonException:
            print('Shop: Beginning the closing sequence.')
            closing = True

@process
def worldSink(fromShop):
    customersTurnedAway = 0
    customersTrimmed = 0
    try:
        while True:
            customer = fromShop()
            if isinstance(customer, Customer):
                customersTurnedAway += 1
                print('World: Customer ' + str(customer.id) + ' exiting the shop, turned away.')
            elif isinstance(customer, SuccessfulCustomer):
                customersTrimmed += 1
                print('World: Customer ' + str(customer.c.id) + ' exiting the shop, trimmed.')
            else:
                raise ValueError('Incorrect return from AltSelect.')
    except ChannelPoisonException:
        print('\nTrimmed ' + str(customersTrimmed) + ' and turned away ' + str(customersTurnedAway) + ' today.')

@process
def worldSource(numberOfCustomers, nextCustomerWaitTime, toShop):
    for i in range(numberOfCustomers):
        time.sleep(nextCustomerWaitTime())
        print('World: Customer ' + str(i) + ' enters the shop.')
        toShop(Customer(i))
    poison(toShop)

def runSimulation(numberOfCustomers, numberOfWaitingSeats, nextCustomerWaitTime, hairTrimTime):
    worldToShop = Channel()
    shopToBarber = Channel()
    barberToShop = Channel()
    shopToWorld = Channel()
    Parallel(
        barber(hairTrimTime, shopToBarber.reader(), barberToShop.writer()),
        shop(numberOfWaitingSeats, worldToShop.reader(), shopToBarber.writer(), barberToShop.reader(), shopToWorld.writer()),
        worldSink(shopToWorld.reader()),
        worldSource(numberOfCustomers, nextCustomerWaitTime, worldToShop.writer()))

if __name__ == '__main__':
    runSimulation(20,  4, lambda: random.random() * 0.002 + 0.001, lambda: random.random() * 0.006 + 0.001)

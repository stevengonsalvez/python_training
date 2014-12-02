#! /usr/bin/env python3
# -*- coding:utf-8; -*-

#  This is a model of the "The Sleeping Barber" problem using Python-CSP,
#  cf. http://en.wikipedia.org/wiki/Sleeping_barber_problem.
#
#  Copyright © 2009–2012 Russel Winder

#  The barber's shop and the barber are modelled with processes.  Channels are used to pass customer objects
#  from the shop to the barber.  The current arrangement assumes there is only one barber.

#  This should work with both Python 2 and Python 3.  Use range everywhere, even where with Python 2 xrange
#  would be preferred so as to ensure it all works with both versions.

import time
import random

from csp.os_process import process, Channel, Par, Alt, ChannelPoison
from csp.guards import Timer

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
            customer = fromShop.read()
            assert isinstance(customer, Customer)
            print('Barber: Starting Customer ' + str(customer.id))
            time.sleep(hairTrimTime())
            customersTrimmed += 1
            print('Barber: Finished Customer ' + str(customer.id))
            toShop.write(SuccessfulCustomer(customer))
    except ChannelPoison:
        print('Barber: Finished work for the day, trimmed ' + str(customersTrimmed))

@process
def shop(numberOfWaitingSeats, fromWorld, toBarber, fromBarber, toWorld):
    seats = []
    customersTrimmed = 0
    customersTurnedAway = 0
    closing = False
    while True:
        try:
            customer = fromBarber | fromWorld
            if isinstance(customer, Customer):
                if len(seats) <= numberOfWaitingSeats:
                    seats.append(customer)
                    print('Shop: Customer ' + str(customer.id) + ' takes a seat. ' + str(len(seats)) + ' in use.')
                    toBarber.write(customer)
                else:
                    customersTurnedAway += 1
                    print('Shop: Customer ' + str(customer.id) + ' turned away.')
                    toWorld.write(customer)
            elif isinstance(customer, SuccessfulCustomer):
                seatsTaken -= 1
                customersTrimmed += 1
                print('Shop: Customer ' + str(customer.c.id) + ' leaving trimmed.')
                toWorld.write(customer)
            else:
                raise ValueError('Shop: select failed, got a ' + str(customer))
            if len(seats) > 0:
                alt = Alt(toBarber, Timer().sleep(0.1))
                toBarber.write(seats[0])
                del(seats[0])
            else:
                if closing:
                    toBarber.poison()
                    print('Shop: Closing -- ' + str(customersTrimmed) + ' trimmed, and ' + str(customersTurnedAway) + ' turned away.')
                    toWorld.poison()
                    break
        except ChannelPoison:
            closing = True

@process
def worldSink(fromShop):
    customersTurnedAway = 0
    customersTrimmed = 0
    try:
        while True:
            customer = fromShop.read()
            if isinstance(customer, Customer):
                customersTurnedAway += 1
                print('World: Customer ' + str(customer.id) + ' exiting the shop, turned away.')
            elif isinstance(customer, SuccessfulCustomer):
                customersTrimmed += 1
                print('World: Customer ' + str(customer.c.id) + ' exiting the shop, trimmed.')
            else:
                raise ValueError('Incorrect return from Alt.')
    except ChannelPoison:
        print('\nTrimmed ' + str(customersTrimmed) + ' and turned away ' + str(customersTurnedAway) + ' today.')

@process
def worldSource(numberOfCustomers, nextCustomerWaitTime, toShop):
    for i in range(numberOfCustomers):
        time.sleep(nextCustomerWaitTime())
        print('World: Customer ' + str(i) + ' enters the shop.')
        toShop.write(Customer(i))
    toShop.poison()

def runSimulation(numberOfCustomers, numberOfWaitingSeats, nextCustomerWaitTime, hairTrimTime):
    worldToShop = Channel()
    shopToBarber = Channel()
    barberToShop = Channel()
    shopToWorld = Channel()
    Par(
        barber(hairTrimTime, shopToBarber, barberToShop),
        shop(numberOfWaitingSeats, worldToShop, shopToBarber, barberToShop, shopToWorld),
        worldSink(shopToWorld),
        worldSource(numberOfCustomers, nextCustomerWaitTime, worldToShop)
        ).start()

if __name__ == '__main__':
    runSimulation(20,  4, lambda: random.random() * 0.002 + 0.001, lambda: random.random() * 0.006 + 0.001)

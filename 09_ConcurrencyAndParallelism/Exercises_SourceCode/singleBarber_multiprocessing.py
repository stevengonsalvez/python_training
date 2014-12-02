#! /usr/bin/env python3

#  This is a model of the "The Sleeping Barber" problem using Python and the multiprocessing package,
#  cf. http://en.wikipedia.org/wiki/Sleeping_barber_problem.
#
#  Copyright © 2009–2012 Russel Winder

#  The world, barber's shop and the barber are modelled using processes each with their own queue -- though
#  the barber queue is actually in the shop.  In effect this is an Actor Model reactor approach with each
#  process using a blocking read on its queue.  The waiting seats are modelled by the barber's queue.

import multiprocessing
try:
    import queue  # Python 3
except:
    import Queue as queue  # Python 2
import time
import random

class Customer(object):
    def __init__(self, id):
        self.id = id

class SuccessfulCustomer(object):
    def __init__(self, customer):
        self.c = customer

_closing = 'closing'
_clockedOff = 'clockedOff'
_closed = 'closed'

class Barber(multiprocessing.Process):
    def __init__(self, hairTrimTime):
        super().__init__()
        self.shop = None  # This value will be injected after construction.
        self.hairTrimTime = hairTrimTime

    def run(self):
        customersTrimmed = 0
        while True:
            customer = self.shop.waitingSeats.get()  # Block on the shop's waiting seats queue.
            if isinstance(customer, Customer):
                print('Barber: Starting Customer ' + str(customer.id))
                time.sleep(self.hairTrimTime())
                customersTrimmed += 1
                print('Barber: Finished Customer ' + str(customer.id))
                self.shop.queue.put(SuccessfulCustomer(customer))
            elif isinstance(customer, str) and customer == _closing:
                print('Barber: Clocking off, trimmed ' + str(customersTrimmed) + 'today.')
                self.shop.queue.put(_clockedOff)
                break
            else:
                raise ValueError('Barber: Unexpected object received:' + str(customer) + ' / ' + str(type(customer)))

class Shop(multiprocessing.Process):
    def __init__(self, numberOfWaitingSeats, barber, world):
        super().__init__()
        self.waitingSeats = multiprocessing.Queue(numberOfWaitingSeats)
        self.barber = barber
        self.world = world
        self.queue = multiprocessing.Queue()

    def run(self):
        customersTrimmed = 0
        customersTurnedAway = 0
        while True:
            customer = self.queue.get()
            if isinstance(customer, Customer):
                try:
                    self.waitingSeats.put_nowait(customer)
                    print('Shop: Customer ' + str(customer.id) + ' takes a seat. ' + str(self.waitingSeats.qsize()) + ' in use.')
                except queue.Full:
                    customersTurnedAway += 1
                    print('Shop: Customer ' + str(customer.id) + ' turned away.')
                    self.world.queue.put(customer)
            elif isinstance(customer, SuccessfulCustomer):
                assert isinstance(customer.c, Customer)
                customersTrimmed += 1
                print('Shop: Customer ' + str(customer.c.id) + ' leaving trimmed.')
                self.world.queue.put(customer)
            elif isinstance(customer, str) and customer == _closing:
                self.waitingSeats.put(customer)
            elif isinstance(customer, str) and customer == _clockedOff:
                print('Shop: Closing --- ' + str(customersTrimmed) + ' trimmed and ' + str(customersTurnedAway) + ' turned away.')
                self.world.queue.put(_closed)
                break
            else:
                raise ValueError('Shop: Unexpected object received:' + str(customer) + ' / ' + str(type(customer)))

class World(multiprocessing.Process):
    def __init__(self):
        super().__init__()
        self.queue = multiprocessing.Queue()

    def run(self):
        customersTrimmed = 0
        customersTurnedAway = 0
        while True:
            customer = self.queue.get()
            if isinstance(customer, Customer):
                customersTurnedAway += 1
                print('World: Customer ' + str(customer.id) + 'exiting the shop, turned away.')
            elif isinstance(customer, SuccessfulCustomer):
                customersTrimmed += 1
                print('World: Customer ' + str(customer.c.id) + ' exiting the shop, trimmed.')
            elif isinstance(customer, str) and customer == _closed:
                print('\nTrimmed ' + str(customersTrimmed) + ' and turned away ' + str(customersTurnedAway) + ' today.')
                break
            else:
                raise ValueError('World: Unexpected object received:' + str(customer) + ' / ' + str(type(customer)))

def runSimulation(numberOfCustomers, numberOfWaitingSeats, nextCustomerWaitTime, hairTrimTime):
    barber = Barber(hairTrimTime)
    world = World()
    shop = Shop(numberOfWaitingSeats, barber, world)
    barber.shop = shop
    barber.start()
    world.start()
    shop.start()
    #  In Python 2 would use xrange here but use range for Python 3 compatibility.
    for i in range(numberOfCustomers):
        time.sleep(nextCustomerWaitTime())
        print('World: Customer ' + str(i) + ' enters the shop.')
        shop.queue.put(Customer(i))
    shop.queue.put(_closing)
    #  Wait for the world to end.
    world.join()

if __name__ == '__main__':
    runSimulation(20,  4, lambda: random.random() * 0.002 + 0.001, lambda: random.random() * 0.006 + 0.001)

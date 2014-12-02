#! /usr/bin/env python3
# -*- coding:utf-8; -*-

from __future__ import print_function

'''A script that creates a multicast listener on the named group and port.'''

__author__ = 'Russel Winder'
__date__ = '2013-09-06'
__version__ = '1.2'
__copyright__ = 'Copyright © 2007, 2012, 2013  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

from multicastGroupSpecification import group, port

class MulticastListener(DatagramProtocol):
    def startProtocol(self):
        print('Started listening on {}:{}'.format(group, port))
        self.transport.joinGroup(group)

    def datagramReceived(self, datagram, address):
        print('Received from {}: {}'.format(address, datagram))

if __name__ == '__main__':
    reactor.listenMulticast(port, MulticastListener())
    reactor.run()

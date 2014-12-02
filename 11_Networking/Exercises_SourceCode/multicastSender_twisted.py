#! /usr/bin/env python3
# -*- coding:utf-8; -*-

from __future__ import print_function

'''A script that sends out a multicast packet to the group and port that the listener is listening to.'''

__author__ = 'Russel Winder'
__date__ = '2013-09-06'
__version__ = '1.1'
__copyright__ = 'Copyright © 2007, 2013  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

from multicastGroupSpecification import group, port

class MulticastSender(DatagramProtocol):
    def startProtocol(self):
        print('Sending to {}:{} with TTL {}.'.format(group, port, self.transport.getTTL()))
        self.transport.write(b'Sent using Twisted.', (group, port))

if __name__ == '__main__':
    reactor.listenMulticast(0, MulticastSender())

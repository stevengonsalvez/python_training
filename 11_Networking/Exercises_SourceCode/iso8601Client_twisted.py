#! /usr/bin/env python3
# -*- coding:utf-8; -*-

from __future__ import print_function

'''
A module providing a Twisted Internet TCP client for the current date
and time in ISO 8601 format on port 8601 server.
'''

__author__ = 'Russel Winder'
__date__ = '2014-07-11'
__version__ = '1.3'
__copyright__ = 'Copyright © 2007, 2012–2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import sys

from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory, Protocol

class TimeClientProtocol(Protocol):
    def connectionMade(self):
        peer = self.transport.getPeer()
        print('Connection made to: {}:{}'.format(peer.host, peer.port))

    def dataReceived(self, data):
        print('Received:', data.decode())
        self.transport.loseConnection()
        reactor.callLater(0, reactor.stop)

class TimeClientFactory(ClientFactory):
    protocol = TimeClientProtocol

if __name__ == '__main__':
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 8601
    address = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
    reactor.connectTCP(address, port, TimeClientFactory())
    print('Connecting to {}:{}'.format(address, port))
    reactor.run()

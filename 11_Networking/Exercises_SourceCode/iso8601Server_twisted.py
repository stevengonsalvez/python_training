#! /usr/bin/env python3
# -*- coding:utf-8; -*-

from __future__ import print_function

'''
A script providing a Twisted Internet TCP server of the current date and
time in ISO 8601 format on port 8601.
'''

__author__ = 'Russel Winder'
__date__ = '2014-07-11'
__version__ = '1.3'
__copyright__ = 'Copyright © 2007, 2012–2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory, Protocol

from formatNow import formatNow

from datetime import datetime, timezone, timedelta

class TimeServerProtocol(Protocol):
    def connectionMade(self):
        print('Connection from: {}'.format(self.transport.getPeer().host))
        self.transport.write(formatNow().encode())
        self.transport.loseConnection()

class TimeServerFactory(ServerFactory):
    protocol = TimeServerProtocol

if __name__ == '__main__':
    socketAddress = ('', 8601)
    reactor.listenTCP(socketAddress[1], TimeServerFactory())
    print('Serving on {}:{}'.format(*socketAddress))
    reactor.run()

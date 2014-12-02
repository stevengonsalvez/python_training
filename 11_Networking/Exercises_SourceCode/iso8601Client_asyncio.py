#! /usr/bin/env python3

'''
A module providing an Asyncio TCP client for the current date
and time in ISO 8601 format on port 8601 server.
'''

__author__ = 'Russel Winder'
__date__ = '2014-07-16'
__version__ = '1.0'
__copyright__ = 'Copyright © 2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import asyncio
import sys

class Client(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        print('Connected to {}'.format(transport.get_extra_info('peername')))

    def data_received(self, data):
        print('Received: {}'.format(data.decode()))
        loop.stop()

address = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
loop = asyncio.get_event_loop()
client = loop.run_until_complete(loop.create_connection(Client, address, 8601))
try:
    loop.run_forever()
except KeyboardInterrupt:
    print('Got a keyboard interrupt so terminating.')
finally:
    loop.close()

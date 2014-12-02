#! /usr/bin/env python3

'''
A module providing an Asyncio TCP server for the current date
and time in ISO 8601 format on port 8601 server.
'''

__author__ = 'Russel Winder'
__date__ = '2014-07-16'
__version__ = '1.0'
__copyright__ = 'Copyright © 2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import asyncio

from formatNow import formatNow

class Server(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        print('Connection from {}'.format(transport.get_extra_info('peername')))
        transport.write(formatNow().encode())

loop = asyncio.get_event_loop()
server = loop.run_until_complete(loop.create_server(Server, '', 8601))
print('Serving od {}:{}'.format()
try:
    loop.run_forever()
except KeyboardInterrupt:
    print('Got a keyboard interrupt so terminating.')
finally:
    server.close()
    loop.close()

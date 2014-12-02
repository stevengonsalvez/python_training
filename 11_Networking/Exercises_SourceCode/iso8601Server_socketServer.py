#! /usr/bin/env python3

'''
A module providing a socket server based server of the current date and
time in ISO 8601 format on port 8601.
'''

__author__ = 'Russel Winder'
__date__ = '2014-07-11'
__version__ = '1.2'
__copyright__ = 'Copyright © 2007, 2012, 2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import socketserver

import formatNow

class TimeHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print('Connection from: ', self.client_address)
        self.wfile.write(formatNow.formatNow().encode())

if __name__ == '__main__':
    socketAddress = ('', 8601)
    server = socketserver.TCPServer(socketAddress, TimeHandler)
    print('Serving on {}:{}'.format(*socketAddress))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('Got a keyboard interrupt so terminating.')
        server.shutdown()  # Should be unecessary.

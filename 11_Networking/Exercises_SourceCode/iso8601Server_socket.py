#! /usr/bin/env python3

'''
A module providing a socket-based server of the current date and time in
ISO 8601 format on port 8601.
'''

__author__ = 'Russel Winder'
__date__ = '2014-07-11'
__version__ = '1.2'
__copyright__ = 'Copyright © 2007, 2012, 2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

from contextlib import contextmanager
import socket

from formatNow import formatNow

@contextmanager
def ensureConnectionCloses(datum):
    try:
        yield datum
    finally:
        datum[0].close()

if __name__ == '__main__':
    socketAddress = ('', 8601)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(socketAddress)
        s.listen(5)
        print('Serving on {}:{}'.format(*socketAddress))
        try:
            while True:
                with ensureConnectionCloses(s.accept()) as (connection, address):
                    print('Connection from:', address)
                    connection.send(formatNow().encode())
        except KeyboardInterrupt:
            print('Got a keyboard interrupt so terminating.')

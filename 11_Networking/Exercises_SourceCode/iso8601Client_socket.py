#! /usr/bin/env python3

'''
A script for making a connection to localhost:8601 and receiving the data sent.
Assumes there will be <1024 bytes of data.
'''

__author__ = 'Russel Winder'
__date__ = '2014-07-11'
__version__ = '1.2'
__copyright__ = 'Copyright © 2007, 2012, 2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import socket
import sys

if __name__ == '__main__':
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 8601
    address = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
    socketAddress = (address, port)
    with socket.create_connection(socketAddress) as s:
        print('Connecting to {}:{}'.format(*socketAddress))
        while True:
            data = s.recv(1024)
            if data:
                print('Received:', data.decode(), sep=None)
            else:
                break
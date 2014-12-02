#! /usr/bin/env python3

'''A script that creates a multicast listener on the named group and port.'''

__author__ = 'Russel Winder'
__date__ = '2012-01-21'
__version__ = '1.1'
__copyright__ = 'Copyright © 2007,2012 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import socket
import struct

from multicastGroupSpecification import group, port

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        ####s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', port))
        mreq = struct.pack('4sl', socket.inet_aton(group), socket.INADDR_ANY)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        try:
            print('Started listening on {}:{}...'.format(group, port))
            while True:
                data, address = s.recvfrom(1024)
                print('Connection from:', address, ':', data.decode())
        except:
            pass

#! /usr/bin/env python3

'''
A script for sending a multicast packet on group as defined in the module multicastGroupSpecification.
Ensure the TTL is small to avoid the packet escaping into the wild.
'''

__author__ = 'Russel Winder'
__date__ = '2012-01-21'
__version__ = '1.1'
__copyright__ = 'Copyright © 2007,2012 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import socket

from multicastGroupSpecification import group, port

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        print('Sending to {}:{} with TTL {}.'.format(group, port, s.getsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL)))
        s.sendto('Sent using sockets directly.'.encode(), (group, port))

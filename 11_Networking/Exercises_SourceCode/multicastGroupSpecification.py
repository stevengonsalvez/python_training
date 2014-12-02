# -*- coding:utf-8; -*-

'''Specification of the multicast group with which to work.'''

__author__ = 'Russel Winder'
__date__ = '2010-09-29'
__version__ = '1.1'
__copyright__ = 'Copyright © 2007, 2010  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

#  224.x.x.x upwards is the multicast address area.  Many multicast addresses are blocked by firewalls.
#  This leads to "Operation not permitted" A subset of the multicast addresses (239.0.0.0 upwards) is deemed
#  "local" (cf. the NATable unicast addresses) and these do not get blocked, so use them.

group = '239.3.2.1'
port = 58000

# -*- coding:utf-8; -*-

'''
A module providing a function that generates the current date and time in ISO 8601 format.
'''

__author__ = 'Russel Winder'
__date__ = '2014-07-11'
__version__ = '1.2'
__copyright__ = 'Copyright © 2007, 2012, 2014 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

from datetime import datetime, timedelta, tzinfo
from time import altzone, daylight, timezone

# Python 3.2 onwards provides a fixed offset timezone type. If using an earlier Python, such a thing must be
# manually constructed.

# NB FixedOffset just needs to be a callable, it doesn't matter if it is a function or a class. Don't you
# just love dynamic languages :-)

try:
    from datetime import timezone
    def FixedOffset(minutes):
        return timezone(timedelta(minutes=minutes))
except:
    #  The following class is based on the one presented in the Python manual.
    #  It needs a lot work to be really viable but does for now.
    class FixedOffset(tzinfo):
        '''
        Fixed offset in minutes east from UTC.
        '''

        def __init__(self, offset):
            self.__offset = timedelta(minutes=offset)

        def utcoffset(self, dt):
            return self.__offset

        def tzname(self, dt):
            return '±XX:XX'

        def dst(self, dt):
            return timedelta(0)


def formatNow():
    '''
    Returns the current date/time in ISO 8601 format.
    '''
    return datetime.now(FixedOffset(-(timezone if daylight == 0 else altzone) / 60)).replace(microsecond=0).isoformat()

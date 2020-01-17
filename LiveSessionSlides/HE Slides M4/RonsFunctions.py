#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RON'S FUNCTIONS
"""
#%%
from datetime import datetime
#%%
def get_datetime(dt_str):
    '''
    Convert dt_str to datetime object
    Return: datetime object
    '''
    try:
        #'2019-03-31 13:00:00'
        return datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    except:
        pass
    try:
        #'03/31/2019'
        return datetime.strptime(dt_str, '%m/%d/%Y')
    except:
        pass
    try:
        #'Mar 31, 2019'
        return datetime.strptime(dt_str, '%b %d, %Y')
    except:
        pass
    try:
        #'31.03.2019'
        return datetime.strptime(dt_str, '%d.%m.%Y')
    except:
        pass

    print ("Can't convert", dt_str)
    return None
#%%
import random
import time

def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)

print(random_date("1/1/2008 1:30 PM", "1/1/2009 4:50 AM", random.random()))
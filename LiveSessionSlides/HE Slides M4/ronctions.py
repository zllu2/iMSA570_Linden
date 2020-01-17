#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RON'S FUNCTIONS
"""
#%%
from datetime import datetime
import numpy as np
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
        #'2019-03-31 13:00' I added this
        return datetime.strptime(dt_str, '%Y-%m-%d %H:%M')
    except:
        pass
    try:
        #'03/31/2019'
        return datetime.strptime(dt_str, '%m/%d/%Y')
    except:
        pass
    try:
        #'03/31/2019 13:00' I added this
        return datetime.strptime(dt_str, '%m/%d/%Y %H:%M')
    except:
        pass
    try:
        #'03/31/19 13:00' I added this
        return datetime.strptime(dt_str, '%m/%d/%y %H:%M')
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
#%% Function to create a random date
def rand_date(startDateSt, endDateSt):
    startDate = get_datetime(startDateSt)
    endDate = get_datetime(endDateSt)
    randDate = startDate + (endDate-startDate)*np.random.rand(1)
    return randDate
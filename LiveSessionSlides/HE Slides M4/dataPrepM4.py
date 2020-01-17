#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exploring Craigslist data on used cars
"""

########## MODULE 4 ##############
# First, walk through how to create a datetime object from strings.
# Show what happens if the try except portions aren't there.
# Review the function from 4.1 notebook to convert strings to dates
# Challenge them to extend that function by including another date format.
# Create a module are the datetime converter from the 4.1 notebook.
# Add a simple hello world type function.
# Show them how to save it to a local directory and then import it into a script in Spyder and Notebooks
# Import and cleanse data from two different files. Combine them. Create fake data.
# Show the split, apply, combine approach based on a variety of date formats used.

#%%
import pandas as pd
import numpy as np
import datetime
import sys
sys.path.append('/Users/rnguymon/Box Sync/PythonScripts')
import ronctions as rf
import os
#%%
# Read in this Kaggle dataset: https://www.kaggle.com/austinreese/craigslist-carstrucks-data/data
v = pd.read_csv('vehicles.csv')
os.system('say "your file has been read in"')
# Windows
#import winsound
#duration = 1000  # milliseconds
#freq = 440  # Hz
#winsound.Beep(freq, duration)
#%% Summary dataset
vsum = v.groupby('state').count()
#%% Reduced list for class analysis
vil = v[(v.state == 'il')].copy()
vut = v[(v.state == 'ut')].copy()
vnv = v[(v.state == 'nv')].copy()
vsmall = pd.concat([vil, vut, vnv], ignore_index = True)
vsmall.condition.unique()
vsmall.dtypes
#%% There aren't any dates, so add in some random dates from the past month
vsmall['datePosted'] = [rf.rand_date('2019-12-01 00:00:01', '2020-01-09 12:00:01')[0] for x in range(vsmall.shape[0]) ]
############# CHANGE THE DATA TO PROVIDE WRANGLING TASKS FOR STUDENTS #############
# Convert the dates to different string formats for each state
# Change the case of the vehicle condition
# Divide up the data into a separate file for each state
#%% Convert the dates to different types of strings for each state
vil = vsmall[(vsmall.state == 'il')].copy()
vil['datePosted'] = vil['datePosted'].apply(lambda x: x.strftime('%Y-%m-%d %H:%M'))
vut = vsmall[(vsmall.state == 'ut')].copy()
vut['datePosted'] = vut['datePosted'].apply(lambda x: x.strftime('%m/%d/%y %H:%M'))
vnv = vsmall[(vsmall.state == 'nv')].copy()
vnv['datePosted'] = vnv['datePosted'].apply(lambda x: x.strftime('%d/%m/%y %H:%M'))
#%% Create some variation in the vehicle condition
vut.loc[:,'condition'] = vut.loc[:,'condition'].str.title()
vnv.odometer.fillna(999999999, inplace = True)
vnv.odometer = vnv.odometer.astype(int)
vil.year = vil.year.astype(str)
vil.rename(columns = {'manufacturer': 'Manufacturer'}, inplace = True)
#%% Write the files
vil.to_csv('/Users/rnguymon/Box Sync/(iMSA Specialization 4) Data Analytics Courses/iMSA ACCY 576/HE Material/Live Session Slides/HE Slides M4/carsTrucksIl.csv', index = False)
vut.to_csv('/Users/rnguymon/Box Sync/(iMSA Specialization 4) Data Analytics Courses/iMSA ACCY 576/HE Material/Live Session Slides/HE Slides M4/carsTrucksUt.csv', index = False)
vnv.to_csv('/Users/rnguymon/Box Sync/(iMSA Specialization 4) Data Analytics Courses/iMSA ACCY 576/HE Material/Live Session Slides/HE Slides M4/carsTrucksNv.csv', index = False)
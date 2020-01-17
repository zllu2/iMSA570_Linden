#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 11:32:50 2020

@author: rnguymon
"""
############ MODULE 3 ################
# This script will take journal entry data and visualize changes in A/R over time.
# This script is meant to have errors in it that students will try to eliminate.
#%% Import libraries
import pandas as pd
#%% Read in the data.
j = pd.read_excel('JournalRaw.xlsx')
#%% Remove top and bottom rows
j2 = j.copy()
j2.columns = j2.iloc[3,]
j2 = j2.iloc[4:j2.shape[0]-3,1:]
#j2 = j2.rename(columns = lambda x: re.sub(' ', '', x))
#%% Create a list of the column names
colNames = j2.columns.values.tolist()
#%% Create tidy, snake_case column names (all lower case, underscore to replace spaces and punctuation)
# Add a print statement at the end of the inner loop to see where it's going wrong.
newColNames = []
for name in colNames:
    tempName = ''
    for letterIndex in range(len(name)):
        tempLetter = name[letterIndex]
        if tempLetter == ' ' or tempLetter == '/': # Remove the part after the or
            tempLetter = '_'
        else:
            tempLetter = tempLetter.lower()
        tempName = tempName + tempLetter # Remove this line
    newColNames.append(tempName) # Remove this line
print(newColNames) # Remove this line
#%% Create tidy, snake_case column names more efficiently
newColNames = []
for name in colNames:
    tempName = name.lower()
    tempName = tempName.replace(' ', '_') # Remove this line
    tempName = tempName.replace('/', '_') # Remove this line
    newColNames.append(tempName)
print(newColNames) # Remove this line
#%% Create tidy, camelCase column names (lower first letter, no spaces or punctuation)
newColNames = []
for name in colNames:
    tempName = name.title() # Remove this line
    tempName = tempName.replace(' ', '')
    tempName = tempName.replace('/', '')
    tempFirstLetter = tempName[0] # Remove this line
    tempFirstLetter = tempFirstLetter.lower() # Remove this line
    tempName = tempName[1:]
    tempName = tempFirstLetter + tempName
    newColNames.append(tempName) # Remove this line
print(newColNames) # Remove this line
#%% Turn the loop that you just created into a function, and then run it. 
#Remove everything.
def camel_case_conversion(listOfNames):
    newColNames = []
    for name in listOfNames:
        tempName = name.title()
        tempName = tempName.replace(' ', '')
        tempName = tempName.replace('/', '')
        tempFirstLetter = tempName[0]
        tempFirstLetter = tempFirstLetter.lower()
        tempName = tempName[1:]
        tempName = tempFirstLetter + tempName
        newColNames.append(tempName)
    return newColNames
camel_case_conversion(['Ron Guymon', 'todd murdock'])
#%% Replace column names on j2 with newColNames
j2.columns = newColNames
#%% Reset index
j2.reset_index(drop = True, inplace = True)
#%% Other tasks: remove blank and summary rows.
newCol = []
for row in range(j2.shape[0]):
    if pd.isnull(j2.loc[row,'debit']) and pd.isnull(j2['credit'].iloc[row]):
        newCol.append('deleteMe')
    elif j2.loc[row,'debit'] == j2.loc[row,'credit']:
        newCol.append('deleteMe') # Remove this line
    else:
        newCol.append('keepMe') # Remove this line
j2['keep'] = newCol
j3 = j2.query('keep == "keepMe"').copy()
j3.drop(columns = 'keep', inplace = True)
#%% Add a new column equal to the value, and a new column to contain whether it's a debit or a credit
j3.reset_index(drop = True, inplace = True)
value = []
dorc = []
for row in range(j3.shape[0]):
    if pd.isnull(j3.loc[row,'debit']) and pd.notnull(j3.loc[row,'credit']):
        value.append(j3.loc[row,'credit'])
        dorc.append('credit') # Remove this line
    else:
        value.append(j3.loc[row,'debit'])
        dorc.append('debit') # Remove this line
j3['value'] = value
j3['dorc'] = dorc
j3.drop(columns = ['debit', 'credit'], inplace = True)
#%% For observations in which there's not a value in the name or num column on the first row of the entry, enter 0
for row in range(j3.shape[0]):
    if pd.notnull(j3.loc[row,'date']):
        if pd.isnull(j3.loc[row,'num']):
            j3.loc[row,'num'] = 0
        if pd.isnull(j3.loc[row,'name']):
            j3.loc[row,'name'] = 'No Name'
#%% Repeat the date, transaction type, transaction number, name, and memo description for each observation.
repCols = ['date', 'transactionType', 'num', 'name']
j3[repCols] = j3[repCols].fillna(method = 'ffill')
#%% Convert the date column to a date format
j3.date = pd.to_datetime(j3.date)
#%% Trial balance to make sure that the debits equal the credits
tb = j3.groupby('dorc').sum()

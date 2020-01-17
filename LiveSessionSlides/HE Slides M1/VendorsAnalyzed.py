#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:41:33 2019

@author: rnguymon
"""

######### CLUSTER ANALYSIS OF THE VENDORS FOR CRAIG'S DESIGN AND LANDSCAPING SERVICES ############3

#%% Libraries
import pandas as pd
#import numpy as np
import re # Regular expressions for dealing with text processing
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
#%% Read in data
# Use the window in the top right of Spyder to set working directory to where the data is located
vr = pd.read_excel('VendorsRaw.xlsx') # vr stands for vendorsRaw
#%% Column names
v = vr.copy()
v.columns = v.iloc[3,]
v = v.iloc[4:v.shape[0]-3,1:]
v = v.rename(columns = lambda x: re.sub(' ', '', x))
v.rename(columns = {'Account#': 'AccountNum'}, inplace = True)
#%% Create a column for each of the three phone numbers: phone, fax, mobile
pnums = v['PhoneNumbers']
pnums = pnums.str.split('\n', n = 3, expand = True)
pnums.columns = ['one', 'two', 'three']
v2 = pd.concat([v, pnums], axis = 1)
v2.reset_index(drop = True, inplace = True)

#%% Test functionality of code to create columns
for row in range(v2.shape[0]):
    print(row)
    if str(v2.loc[row,'one']) != 'nan' and re.search('Fax', str(v2.loc[row,'one'])) is not None:
        print(v2.loc[row, 'one'])
    elif str(v2.loc[row,'two']) != 'nan' and re.search('Fax', str(v2.loc[row, 'two'])) is not None:
        print(v2.loc[row, 'two'])
    elif str(v2.loc[row,'three']) != 'nan' and re.search('Fax', str(v2.loc[row, 'three'])) is not None:
        print(v2.loc[row, 'three'])
    else:
        print('all are missing')

#%% Finish creating a column for each of the three phone numbers
# Phone
v2['phone'] = ''
def phone(row):
    if str(row['one']) != 'nan' and re.search('Phone', str(row['one'])) is not None:
        return re.sub('Phone: ', '', row['one'])
    elif str(row['two']) != 'nan' and re.search('Phone', str(row['two'])) is not None:
        return re.sub('Phone: ', '', row['two'])
    elif str(row['three']) != 'nan' and re.search('Phone', str(row['three'])) is not None:
        return re.sub('Phone: ', '', row['three'])
    
v2['phone'] = v2.apply(phone, axis = 1)
# Fax
v2['fax'] = ''
def fax(row):
    if str(row['one']) != 'nan' and re.search('Fax', str(row['one'])) is not None:
        return re.sub('Fax: ', '', row['one'])
    elif str(row['two']) != 'nan' and re.search('Fax', str(row['two'])) is not None:
        return re.sub('Fax: ', '', row['two'])
    elif str(row['three']) != 'nan' and re.search('Fax', str(row['three'])) is not None:
        return re.sub('Fax: ', '', row['three'])
    
v2['fax'] = v2.apply(fax, axis = 1)
# Mobile
v2['mobile'] = ''
def mobile(row):
    if str(row['one']) != 'nan' and re.search('Mobile', str(row['one'])) is not None:
        return re.sub('Mobile: ', '', row['one'])
    elif str(row['two']) != 'nan' and re.search('Mobile', str(row['two'])) is not None:
        return re.sub('Mobile: ', '', row['two'])
    elif str(row['three']) != 'nan' and re.search('Mobile', str(row['three'])) is not None:
        return re.sub('Mobile: ', '', row['three'])
    
v2['mobile'] = v2.apply(mobile, axis = 1)
v2.drop(columns = ['one', 'two', 'three', 'PhoneNumbers'], inplace = True)
#%% Separate FullName into different columns
# Add a blank column for each part of the name
v3 = v2.copy() 
nameCols = ['title', 'firstName', 'middleName', 'lastName', 'suffix']
for i in nameCols:
    v3[i] = ''

# Function to separate out the name
def sepNames(row):
    tempName = str(row['FullName'])
    if tempName not in ['None', 'nan']:
        # Title
        if re.search('\. ', tempName) is not None:
            title = re.sub('\. .*$', '.', tempName)
            tempName = re.sub(title + ' ', '', tempName)
        else:
            title = ''
        # First name
        firstName = re.sub(' .*$', '', tempName)
        tempName = re.sub('^.*'+firstName+' ', '', tempName)
        # Middle
        middleNameEnd = re.search(' ', tempName)
        if middleNameEnd is not None:
            if middleNameEnd.start() <= 2:
                middleName = tempName[0:middleNameEnd.start()]
                tempName = tempName[middleNameEnd.start()+1:]
            else:
                middleName = ''
        else:
            middleName = ''
        # Suffix
        if re.search(' ', tempName) is not None:
            suffix = re.sub('^.* ', '', tempName)
            tempName = re.sub(' .*$', '', tempName)
        else:
            suffix = ''
        # Last Name
        lastName = tempName
    else:
        title, firstName, middleName, lastName, suffix = ['', '', '', '', '']
    return pd.Series([title, firstName, middleName, lastName, suffix])

#v3.loc[24,nameCols] = sepNames(v3.loc[24,]) # Test one row
v3[nameCols] = v3.apply(sepNames, axis = 1)
v3.drop('FullName', axis = 1, inplace = True)

    
##%% Test name separation functions 
#re.sub('\. .*$', '.', 'Mr. Ron Guymon Esq. ')
##%% Test what would be returned
#v3 = v2.copy()
#for i in range(v3.shape[0]):
#    tempName = str(v3.loc[i, 'FullName'])
#    if tempName not in ['None', 'nan']:
#        # Title
#        if re.search('\. ', tempName) is not None:
#            title = re.sub('\. .*$', '.', tempName)
#            tempName = re.sub(title + ' ', '', tempName)
#        else:
#            title = ''
#        # First name
#        firstName = re.sub(' .*$', '', tempName)
#        tempName = re.sub('^.*'+firstName+' ', '', tempName)
#        # Middle
#        middleNameEnd = re.search(' ', tempName)
#        if middleNameEnd is not None:
#            if middleNameEnd.start() <= 2:
#                middleName = tempName[0:middleNameEnd.start()]
#                tempName = tempName[middleNameEnd.start()+1:]
#            else:
#                middleName = ''
#        else:
#            middleName = ''
#        # Suffix
#        if re.search(' ', tempName) is not None:
#            suffix = re.sub('^.* ', '', tempName)
#            tempName = re.sub(' .*$', '', tempName)
#        else:
#            suffix = ''
#        # Last Name
#        lastName = tempName
#    else:
#        title, firstName, middleName, lastName, suffix = ['', '', '', '', '']
#    print(str(i) + ' ' + str(v3.loc[i, 'FullName']) + ': ' + title + ' '+ firstName  + ' '+ middleName  + ' '+ lastName  + ' '+ suffix)

#%% Separate address into appropriate fields
v4 = v3.copy()
addressCols = ['street', 'city', 'state', 'zip5', 'country']
for i in addressCols:
    v4[i] = ''

def sepAddress(row):
    tempAd = str(row['Address'])
    if tempAd not in ['None', 'nan']:
        #country
        if len(re.findall('\n', tempAd)) > 1:
            country = re.subn('.*\n', '', tempAd)[0]
            tempAd = re.sub('\n.*$', '', tempAd)
        else:
            country = ''
        #street
        street = re.sub('\n.*$', '', tempAd)
        tempAd = re.sub('^.*\n', '', tempAd)
        #zip5
        zip5 = str(tempAd[-5:])
        tempAd = tempAd[:-6]
        #state
        state = tempAd[-2:]
        tempAd = tempAd[:-3]
        #city
        city = tempAd
    else:
        street, city, state, zip5, country = ['', '', '', '', '']
    return pd.Series([street, city, state, zip5, country])
v4[addressCols] = v4.apply(sepAddress, axis = 1)
v4.drop(columns = 'Address', axis = 1, inplace = True)
#%% Create a dataframe for cluster analysis
v5 = v4.copy()
v5 = v5.assign(
        fax = lambda dataframe: dataframe['fax'].map(lambda fax: 1 if fax is not None else 0)
        ).assign(
        lastName = lambda dataframe: dataframe['lastName'].map(lambda lastName: 1 if lastName is not '' else 0)
                ).assign(
                        state = lambda dataframe: dataframe['state'].map(lambda state: state if state is not '' else None)
                        )
v5 = v5[['Vendor', 'fax', 'lastName', 'state']]
# One hot encode the state
v5 = pd.get_dummies(v5, prefix_sep = '_', columns = ['state'])
#%% Cluster analysis elbow plot
rowLabel = v5['Vendor']
clusterData = v5.drop(columns = 'Vendor', axis = 1)
wcss = [] # within cluster sum of squares

for i in range(1,8):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300
                    , n_init = 10, random_state = 0)
    kmeans.fit(clusterData)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 8), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

#%% Create clusters
kmeans = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 300
                    , n_init = 10, random_state = 0)
clusterLabel = kmeans.fit_predict(clusterData)

#%% Add cluster labels to dataframe
v5['cluster'] = clusterLabel
#%% Get centroid values from original data
clusterSum = v5.groupby(['cluster']).mean()
clusterSum.T
#%% Cluster centroid values from model fit
clusterCentroids = pd.DataFrame(kmeans.cluster_centers_.T
                                , columns = ['Cluster_1', 'Cluster_2', 'Cluster_3'])
features = list(clusterSum.columns.values.tolist())
clusterCentroids['Feature'] = features
#%% Plot clusters
plt.plot('Feature', 'Cluster_1', data = clusterCentroids, label = 'Cluster_1')
plt.plot('Feature', 'Cluster_2', data = clusterCentroids, label = 'Cluster_2')
plt.plot('Feature', 'Cluster_3', data = clusterCentroids, label = 'Cluster_3')
plt.title('Cluster Centroid Values')
plt.xlabel('Feature')
plt.ylabel('Value')
plt.legend()
#%% test


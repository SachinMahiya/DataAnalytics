# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 08:37:57 2023

@author: sachi
"""

import pandas as pd

data = pd.read_csv('transaction.csv', sep=';')

data['CostPerTransaction']= data['CostPerItem']*data['NumberOfItemsPurchased']

data['SalesPerTransaction']= data['SellingPricePerItem']*data['NumberOfItemsPurchased']

data['Profit']= data['SalesPerTransaction']-data['CostPerTransaction']

data['Markup']= data['Profit']/data['CostPerTransaction']

data['Markup']= round(data['Markup'], 2)

Day = data['Day'].astype(str)
Year = data['Year'].astype(str)

data['Date']= Day+ '-'+ data['Month']+ '-'+ Year

split_ckw = data['ClientKeywords'].str.split(',', expand=True)

data['ClintAge'] = split_ckw[0]
data['ClintType'] = split_ckw[1]
data['ClintContract'] = split_ckw[2]

data['ClintAge'] = data['ClintAge'].str.replace('[','')
data['ClintContract']= data['ClintContract'].str.replace(']','')

data['ItemDescription'] = data['ItemDescription'].str.lower()

season_value = pd.read_csv('value_inc_seasons.csv', sep=';')

data= pd.merge(data, season_value, on='Month')

data= data.drop(['Day', 'Month', 'Year', 'ClientKeywords'], axis=1)

data.to_csv('Project1Sales.csv', index=False)
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 11:19:43 2023

@author: sachi
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

json_file = open('loan_data_json.json')
data = json.load(json_file)

loandata = pd.DataFrame(data)

loandata['purpose'].unique()

loandata.describe()

loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

length= len(loandata)

ficocat = []
for x in range(0,9577):
    category = loandata['fico'][x]
    if category >= 300 and category < 400:
        cat = 'Very Poor'
    elif category >= 400 and category < 600:
        cat = 'Poor'
    elif category >= 601 and category < 660:
        cat = 'Fair'
    elif category >= 660 and category < 700:
        cat = 'Good'
    elif category >= 700:
        cat = 'Excellent'
    else:
        cat = 'Unknown' 
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)

loandata['fico.category'] =ficocat


loandata.loc[loandata['int.rate'] >0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <=0.12, 'int.rate.type'] = 'Low'


loandata.to_csv('Project2loan.csv', index = True)
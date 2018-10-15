# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 10:10:52 2018

@author: tanay
"""


import pandas as pd
from random import random
import datetime



def random_walk():
    for i in df.index:
        movement = -1 if random() < 0.5 else 1 
        df.loc[i+1,'Data'] = df.loc[i,'Data'] + movement


base_date = datetime.datetime(2018, 1, 1)
no_of_days = 365
index = pd.date_range(base_date, periods=no_of_days-1, freq='D')
df = pd.DataFrame(index=index, columns=['Data'])
df = df.fillna(0)

random_walk()

df.plot()
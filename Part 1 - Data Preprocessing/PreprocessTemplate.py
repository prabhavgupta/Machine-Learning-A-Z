# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 00:15:15 2017

@author: prabhav
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

from sklearn.preprocessing import Imputer 
imputer = Imputer(missing_values='NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[: , 1:3])
X[: , 1:3] = imputer.transform(X[: , 1:3])
print(X)


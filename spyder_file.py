# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%
#importing libraries
#Libraries
import pandas as pd
import numpy as np
import functools
import warnings
import math
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings('ignore')
#%%
import_data = pd.read_csv("https://www4.stat.ncsu.edu/~online/datasets/EDU01a.csv")
import_data.head()
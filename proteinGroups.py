# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:48:41 2015

@author: student
"""

import pandas as pd
#import numpy as np

# read in file
df = pd.read_table('/Users/student/Desktop/pubs/Sample text files/proteinGroups.txt', index_col=0)
#print df.dtypes
print df['Intensity']
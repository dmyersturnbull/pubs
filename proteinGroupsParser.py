# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 08:46:25 2015

@author: student
"""

import pandas as pd
#import numpy as np

# read in file
#peptideNames = """'Protein IDs’, 'Majority protein IDs’, 'Peptide counts (all)’, 'Peptide counts (razor+unique)’, 'Peptide counts (unique)’, 'Fasta headers’, 'Number of proteins’, 'Peptides’,'Razor + unique peptides’, 'Unique peptides’,'Peptides Control_Ub’, 'Peptides Control_UbP’,'Peptides Control_WCL’, 'Peptides Control_WCLP’,'Peptides Pynd_5FC_Ub’, 'Peptides Pynd_5FC_UbP’,'Peptides Pynd_5FC_WCL’, 'Peptides Pynd_5FC_WCLP’,'Peptides Pynd_AlkKO_Ub’, 'Peptides Pynd_AlkKO_UbP’,'Peptides Pynd_AlkKO_WCL’, 'Peptides Pynd_AlkKO_WCLP’"""
#colIndices = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 18, 19, 20, 21, 38, 39, 40, 41, 42, 43, 44, 45, 68, 69, 70, 71, 88, 89, 90, 91, 92, 93, 94, 95, 118, 119, 120, 121, 138, 139, 140, 141, 142, 143, 144, 145, 160, 161, 162, 163, 164, 165, 166, 167, 176, 177, 178, 179, 196, 197, 198, 199, 200, 201, 202, 203, 226, 227, 228, 229, 246, 247, 248, 249, 250, 251, 252, 253, 268, 277, 278, 279, 280, 297, 298, 299, 300, 301, 302, 303, 304, 327, 328, 329, 330, 347, 348, 349, 350, 351, 352, 353, 354, 377, 378, 379, 380, 397, 398, 399, 400, 401, 402, 403, 404, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433
 
data = '/Users/student/Downloads/PUBS 2015 MS files/proteinGroups.txt'

df = pd.read_table(data, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 18, 19, 20, 21, 38, 39, 40, 41, 42, 43, 44, 45, 68, 69, 70, 71, 88, 89, 90, 91, 92, 93, 94, 95, 118, 119, 120, 121, 138, 139, 140, 141, 142, 143, 144, 145, 160, 161, 162, 163, 164, 165, 166, 167, 176, 177, 178, 179, 196, 197, 198, 199, 200, 201, 202, 203, 226, 227, 228, 229, 246, 247, 248, 249, 250, 251, 252, 253, 268, 277, 278, 279, 280, 297, 298, 299, 300, 301, 302, 303, 304, 327, 328, 329, 330, 347, 348, 349, 350, 351, 352, 353, 354, 377, 378, 379, 380, 397, 398, 399, 400, 401, 402, 403, 404, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433])

# Junk
#print df.dtypes
#print df['Intensity']
#for i in df.index:
#    for j in df.columns:
#        print df.index[i], df.columns[j]
#    print df.index.values
    #print df.columns.values
#print df.keys
#   print '%s, %s' % (df.index.values, df[i].columns.values)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 20:39:02 2017

@author: timschutzlkord
"""


import numpy as np
import pandas as pd
test = pd.read_csv('en_train_lim.csv') 

def numberofdashes(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],3))
    next_element=np.append(a[1:,2],"abc")
    this_element=a[:,2]
    previous_element=np.insert(a[:-1,2],0,"abc")
    dash='-'
    for j in range(1,np.shape(a)[0]+1):
        count = 0
        for k in range(1,len(str(this_element[j-1]))+1):
            if str(this_element[j-1])[k-1] in dash:
                count = count +1
        output[j-1,0]=a[j-1,0]
        output[j-1,1]=a[j-1,1]
        output[j-1,2]=count
    return output
    
test=test.values
output=numberofdashes(test)
output
output1 = pd.DataFrame(output)
output1.to_csv('output1.csv')
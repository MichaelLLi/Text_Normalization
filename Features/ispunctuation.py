#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 15:50:20 2017

@author: timschutzlkord
"""
import numpy as np
import pandas as pd
test = pd.read_csv('en_train_lim.csv')
 
def ispunctuation(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],3))
    next_element=np.append(a[1:,2],"abc")
    this_element=a[:,2]
    previous_element=np.insert(a[:-1,2],0,"abc")
    punctuations=',.-_()+!? :;[]\'\"/'
    for j in range(1,np.shape(a)[0]+1):
        countpunctuations=0
        output[j-1,0]=a[j-1,0]
        output[j-1,1]=a[j-1,1]
        if len(str(this_element[j-1]))==1:
            if str(this_element[j-1]) in punctuations:
                output[j-1,2]=1
            else:
                output[j-1,2]=0
        else:
            output[j-1,2]=0
    return output
    
test=test.values
output=ispunctuation(test)
output
output1 = pd.DataFrame(output)
output1.to_csv('output1.csv')
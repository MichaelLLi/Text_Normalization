#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 19:37:05 2017

@author: timschutzlkord
"""

import numpy as np
import pandas as pd
test = pd.read_csv('en_train_lim.csv')
 
def ismixofnumberandletters(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],3))
    next_element=np.append(a[1:,2],"abc")
    this_element=a[:,2]
    previous_element=np.insert(a[:-1,2],0,"abc")
    numbers='0123456789'
    letters='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    for j in range(1,np.shape(a)[0]+1):
        countnumbers=0
        countletters=0
        for k in range(1,len(str(this_element[j-1]))+1):
            if str(this_element[j-1])[k-1] in numbers:
                countnumbers=countnumbers+1
            if str(this_element[j-1])[k-1] in letters:
                countletters=countletters+1
        output[j-1,0]=a[j-1,0]
        output[j-1,1]=a[j-1,1]
        if (countnumbers>0)&(countletters>0):
            output[j-1,2]=1
        else:
            output[j-1,2]=0
    return output
    
test=test.values
output=ismixofnumberandletters(test)
output
output1 = pd.DataFrame(output)
output1.to_csv('output1.csv')
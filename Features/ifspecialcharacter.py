#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:36:53 2017

@author: timschutzlkord, checked
"""

import numpy as np
import pandas as pd
test = pd.read_csv('en_train_lim.csv')
 
def ifspecialcharacter(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],3))
    next_element=np.append(a[1:,2],"abc")
    this_element=a[:,2]
    previous_element=np.insert(a[:-1,2],0,"abc")
    notspecialcharacter='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789,.-_()+!? :;[]\'\"/'
    isstrlen_this_element=np.zeros(shape=(np.shape(a)[0],1))
    isspecialcharacter_this_element=np.zeros(shape=(np.shape(a)[0],1))
    for j in range(1,np.shape(a)[0]+1):
        isstrlen_this_element[j-1]=int(len(str(this_element[j-1]))==1)
        isspecialcharacter_this_element[j-1]=int((str(this_element[j-1]) not in notspecialcharacter))
        output[j-1,0]=a[j-1,0]
        output[j-1,1]=a[j-1,1]
        output[j-1,2]=isstrlen_this_element[j-1]*isspecialcharacter_this_element[j-1]
    return output

test=test.values
output=ifspecialcharacter(test)
output
output1 = pd.DataFrame(output)
output1.to_csv('output1.csv')
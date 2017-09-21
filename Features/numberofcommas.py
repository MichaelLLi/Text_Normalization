#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:50:16 2017

@author: timschutzlkord, based on Michael's script
"""

import numpy as np
 
def numberofcommas(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.array(shape=(np.shape(a)[1],3))
    next_element=np.append(a[1:,3],"abc")
    this_element=a[:,3]
    previous_element=np.insert(a[:-1,3],0,"abc")
    comma=','
    for j in range(1,np.shape(a)[1]):
        count = 0
        for k in range(1,len(this_element[j-1])):
            if this_element[j-1][k-1] in comma:
                count = count +1
        output[j-1,1]=a[j-1,1]
        output[j-1,2]=a[j-1,2]
        output[j-1,3]=count
    return output
    

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 19:37:05 2017

@author: timschutzlkord
"""

import numpy as np
 
def ismixofnumberandletter(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.array(shape=(np.shape(a)[1],3))
    next_element=np.append(a[1:,3],"abc")
    this_element=a[:,3]
    previous_element=np.insert(a[:-1,3],0,"abc")
    numbers='0123456789'
    letters='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    for j in range(1,np.shape(a)[1]):
        countnumbers=0
        countletters=0
        for k in range(1,len(this_element[j-1])):
            if this_element[j-1][k-1] in numbers:
                countnumbers=countnumbers+1
            if this_element[j-1][k-1] in letters:
                countletters=countletters+1
        output[j,1]=a[j,1]
        output[j,2]=a[j,2]
        if countnumbers+countletters==len(this_element[j-1]):
            output[j,3]=1
        else:
            output[j,3]=0
    return output

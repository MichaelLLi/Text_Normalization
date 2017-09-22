#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:06:11 2017

@author: timschutzlkord, based on Michael's script
"""

import numpy as np
 
def ismixofnumberandpunctuations(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.array(shape=(np.shape(a)[1],3))
    next_element=np.append(a[1:,3],"abc")
    this_element=a[:,3]
    previous_element=np.insert(a[:-1,3],0,"abc")
    numbers=np.array(['0123456789'])
    punctuations=np.array([',.-_()+!? :;[]\'\"/'])
    for j in range(1,np.shape(a)[1]):
        countnumbers=0
        countpunctuations=0
        for k in range(1,len(this_element[j-1])):
            if this_element[j-1][k-1] in numbers:
                countnumbers=countnumbers+1
            if this_element[j-1][k-1] in punctuations:
                countpunctuations=countpunctuations+1
        output[j-1,1]=a[j-1,1]
        output[j-1,2]=a[j-1,2]
        if countnumbers+countpunctuations==len(this_element[j-1]):
            output[j-1,3]=1
        else:
            output[j-1,3]=0
    return output

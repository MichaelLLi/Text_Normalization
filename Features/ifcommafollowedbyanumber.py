#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 20:44:13 2017

@author: timschutzlkord
"""

def ifcommafollowedbynumber(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],3))
    next_element=np.append(a[1:,2],"abc")
    this_element=a[:,2]
    previous_element=np.insert(a[:-1,2],0,"abc")
    comma=','
    numbers='0123456789'
    for j in range(1,np.shape(a)[0]+1):
        identifier = 0
        for k in range(1,len(str(this_element[j-1]))):
            if (str(this_element[j-1])[k-1] in comma)&(str(this_element[j-1])[k] in numbers):
                identifier = 1
        output[j-1,0]=a[j-1,0]
        output[j-1,1]=a[j-1,1]
        output[j-1,2]=identifier
    return output

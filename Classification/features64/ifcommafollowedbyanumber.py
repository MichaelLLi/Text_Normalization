#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 20:44:13 2017

@author: timschutzlkord
"""
import numpy as np


def ifcommafollowedbynumber(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],3))
    next_element=np.append(a[1:,2],"abc")
    this_element=a[:,2]
    previous_element=np.insert(a[:-1,2],0,"abc")
    comma=','
    numbers='0123456789'
    for j in range(np.shape(a)[0]):
        output[j,0]=0
        output[j,1]=0
        output[j,2]=0
        for k in (range(1,len(str(next_element[j]))-1)):
            if (str(next_element[j])[k-1] in numbers)&(str(next_element[j])[k] in comma)&(str(next_element[j])[k+1] in numbers):
                output[j,0]=1
        for l in (range(1,len(str(this_element[j]))-1)):
            if (str(this_element[j])[l-1] in numbers)&(str(this_element[j])[l] in comma)&(str(this_element[j])[l+1] in numbers):
                output[j,1]=1
        for m in (range(1,len(str(previous_element[j]))-1)):
            if (str(previous_element[j])[m-1] in numbers)&(str(previous_element[j])[m] in comma)&(str(previous_element[j])[m+1] in numbers):
                output[j,2]=1
    return output

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:57:35 2017

@author: timschutzlkord
"""

import numpy as np

def prepositionfollowedbyanumber(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],3))
    next_element=np.append(a[1:,2],"abc")
    this_element=a[:,2]
    previous_element=np.insert(a[:-1,2],0,"abc")
    numbers='0123456789'
    prepositions=np.array(['on','in','at','since','for','to','before','ago','past','until','till','by','after','from','around','about','of','during'])
    for j in range(np.shape(a)[0]):
        indicatornumber=0
        indicatorpreposition=0
        if str(this_element[j]) in prepositions:
            indicatorpreposition=1
        if str(next_element[j])[0] in numbers:
            indicatornumber=1
        if indicatorpreposition*indicatornumber==1:
            output[j,1]=1
        else:
            output[j,1]=0
    for l in range(2,np.shape(a)[0]+1):
        output[l-1,2]=output[l-2,1]
    for m in range(1,np.shape(a)[0]):
        output[m-1,0]=output[m,1]
    return output

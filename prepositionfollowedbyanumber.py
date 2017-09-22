#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:57:35 2017

@author: timschutzlkord
"""

import numpy as np
 
def prepositionfollowedbyanumber(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.array(shape=(np.shape(a)[1],3))
    next_element=np.append(a[0:,3],"abc")
    this_element=a[:,3]
    previous_element=np.insert(a[:-1,3],0,"abc")
    numbers='0123456789'
    prepositions=np.array(['on','in','at','since','for','to','before','ago','past','until','till','by','after','from','around','about','of','during'])
    for j in range(1,np.shape(a)[1]-1):
        indicatornumber=0
        indicatorpreposition=0
        if this_element[j-1] in preposition:
            indicatorpreposition=1
        if next_element[j-1] in numbers:
            indicatornumber=1
        output[j-1,1]=a[j-1,1]
        output[j-1,2]=a[j-1,2]
        if indicatorpreposition*indicatornumber==1:
            output[j-1,3]=1
        else:
            output[j-1,3]=0
    return output
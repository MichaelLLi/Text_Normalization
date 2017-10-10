#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:50:16 2017

@author: timschutzlkord
"""

import numpy as np
def numberofcommas(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],3))
    next_element=np.append(a[1:,2],"abc")
    this_element=a[:,2]
    previous_element=np.insert(a[:-1,2],0,"abc")
    comma=','
    for j in range(np.shape(a)[0]):
        cnt_next = Counter(str(next_element[j]))
        cnt_this = Counter(str(this_element[j]))
        cnt_prev = Counter(str(previous_element[j]))
        output[j,0]=sum(cnt_next[x] for x in comma)
        output[j,1]=sum(cnt_this[x] for x in comma)
        output[j,2]=sum(cnt_prev[x] for x in comma)
    return output

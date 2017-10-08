#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:10:03 2017

@author: timschutzlkord
"""

from collections import Counter
import numpy as np
 
def ifallcaps(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],3))
    next_element=np.append(a[1:,2],"abc")
    this_element=a[:,2]
    previous_element=np.insert(a[:-1,2],0,"abc")
    caps='QWERTYUIOPASDFGHJKLZXCVBNM'
    for j in range(np.shape(a)[0]):
        cnt_next=Counter(str(next_element[j]))
        cnt_this=Counter(str(this_element[j]))
        cnt_prev=Counter(str(previous_element[j]))           
        output[j,0]=int(sum(cnt_next[x] for x in caps)==len(str(next_element[j])))
        output[j,1]=int(sum(cnt_this[x] for x in caps)==len(str(this_element[j])))
        output[j,2]=int(sum(cnt_prev[x] for x in caps)==len(str(previous_element[j])))
    return output

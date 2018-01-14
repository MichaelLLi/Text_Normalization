#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:59:19 2017

@author: timschutzlkord
"""
from collections import Counter
import numpy as np

def numberofspecialcharacters(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],3))
    next_element=np.append(a[1:,2],"abc")
    this_element=a[:,2]
    previous_element=np.insert(a[:-1,2],0,"abc")
    notspecialcharacter=',.!? :;[]\'\"0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    for j in range(np.shape(a)[0]):
        cnt_next = Counter(str(next_element[j]))
        cnt_this = Counter(str(this_element[j]))
        cnt_prev = Counter(str(previous_element[j]))
        output[j,0]=len(str(next_element[j]))-sum(cnt_next[x] for x in notspecialcharacter)
        output[j,1]=len(str(this_element[j]))-sum(cnt_this[x] for x in notspecialcharacter)
        output[j,2]=len(str(previous_element[j]))-sum(cnt_prev[x] for x in notspecialcharacter)
    return output

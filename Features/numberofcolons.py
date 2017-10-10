#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 20:04:13 2017

@author: timschutzlkord
"""
def numberofcolons(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],3))
    next_element=np.append(a[1:,2],"abc")
    this_element=a[:,2]
    previous_element=np.insert(a[:-1,2],0,"abc")
    colon=':'
    for j in range(np.shape(a)[0]):
        cnt_next = Counter(str(next_element[j]))
        cnt_this = Counter(str(this_element[j]))
        cnt_prev = Counter(str(previous_element[j]))
        output[j,0]=sum(cnt_next[x] for x in colon)
        output[j,1]=sum(cnt_this[x] for x in colon)
        output[j,2]=sum(cnt_prev[x] for x in colon)
    return output

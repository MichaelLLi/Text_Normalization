#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 19:57:05 2017

@author: timschutzlkord
"""

from collections import Counter
import numpy as np
 
def ifallnumbers(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],3))
    next_element=np.append(a[1:,2],"abc")
    this_element=a[:,2]
    previous_element=np.insert(a[:-1,2],0,"abc")
    numbers='0123456789,.'
    negsign='-'
    numbersplusnegsign='0123456789,.-'
    for j in range(np.shape(a)[0]):
        cnt_next=Counter(str(next_element[j]))
        cnt_this=Counter(str(this_element[j]))
        cnt_prev=Counter(str(previous_element[j]))
        nxt=str(next_element[j])[0]
        ths=str(this_element[j])[0]
        prev=str(previous_element[j])[0]
        output[j,0]=int(sum(cnt_next[x] for x in numbers)==len(str(next_element[j])))
        output[j,1]=int(sum(cnt_this[x] for x in numbers)==len(str(this_element[j])))
        output[j,2]=int(sum(cnt_prev[x] for x in numbers)==len(str(previous_element[j])))
        # Take into account of e.g. 1,965 and 5.62 but exclude commas and periods
        if((nxt in ',.')&(len(str(next_element[j]))==1)):
            output[j,0]=0
        if((ths in ',.')&(len(str(this_element[j]))==1)):
            output[j,1]=0
        if((prev in ',.')&(len(str(previous_element[j]))==1)):
            output[j,2]=0
        # We want to keep the negative sign only at the beginning: 
        if((nxt in negsign)&(len(str(next_element[j]))>1)&(sum(cnt_next[x] for x in negsign)==1)&(sum(cnt_next[x] for x in numbersplusnegsign)==len(str(next_element[j])))):
            output[j,0]=1
        if((ths in negsign)&(len(str(this_element[j]))>1)&(sum(cnt_this[x] for x in negsign)==1)&(sum(cnt_this[x] for x in numbersplusnegsign)==len(str(this_element[j])))):
            output[j,1]=1
        if((prev in negsign)&(len(str(previous_element[j]))>1)&(sum(cnt_prev[x] for x in negsign)==1)&(sum(cnt_prev[x] for x in numbersplusnegsign)==len(str(previous_element[j])))):
            output[j,2]=1
    return output

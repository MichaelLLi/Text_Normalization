#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:16:10 2017

@author: timschutzlkord
"""

import numpy as np

def ismixofpunctuationsandletters(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],3))
    next_element=np.append(a[1:,2],"abc")
    this_element=a[:,2]
    previous_element=np.insert(a[:-1,2],0,"abc")
    punctuations=',.!? :;\'\"[]/()《》'
    letters='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    for j in range(1,np.shape(a)[0]+1):
        countpunctuations=0
        countletters=0
        for k in range(1,len(str(this_element[j-1]))+1):
            if str(this_element[j-1])[k-1] in punctuations:
                countpunctuations=countpunctuations+1
            if str(this_element[j-1])[k-1] in letters:
                countletters=countletters+1
        if((countpunctuations+countletters==len(str(this_element[j-1])))&(countpunctuations>=1)&(countletters>=1)):
            output[j-1,1]=1
        else:
            output[j-1,1]=0
    for l in range(2,np.shape(a)[0]+1):
        output[l-1,2]=output[l-2,1]
    for m in range(1,np.shape(a)[0]):
        output[m-1,0]=output[m,1]
    return output

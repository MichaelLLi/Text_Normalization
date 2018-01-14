#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:47:53 2017

@author: timschutzlkord
"""

import numpy as np
import pandas as pd

    
 
def ismixoflettersandspecialcharacters(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],3))
    next_element=np.append(a[1:,2],"abc")
    this_element=a[:,2]
    previous_element=np.insert(a[:-1,2],0,"abc")
    letters='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    punctuationsnumbersandletters=',.-_()+!? :;[]\'\"/0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    for j in range(1,np.shape(a)[0]+1):
        countletters=0
        countspecialcharacters=0
        for k in range(1,len(str(this_element[j-1]))+1):
            if str(this_element[j-1])[k-1] in letters:
                countletters=countletters+1
            if not(str(this_element[j-1])[k-1] in punctuationsnumbersandletters):
                countspecialcharacters=countspecialcharacters+1
        if (countletters+countspecialcharacters==len(str(this_element[j-1])))&(countletters<len(str(this_element[j-1])))&(countspecialcharacters<len(str(this_element[j-1]))):
            output[j-1,1]=1
        else:
            output[j-1,1]=0
    output[:,0]=np.append(output[:,1][1:],0)
    output[:,2]=np.insert(output[:,1][:-1],0,0)
    return output
    
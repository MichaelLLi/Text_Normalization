#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:36:53 2017

@author: timschutzlkord, based on Michael's script
"""

import numpy as np
 
def ifspecialcharacter(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.array(shape=(np.shape(a)[1],3))
    next_element=np.append(a[1:,3],"abc")
    this_element=a[:,3]
    previous_element=np.insert(a[:-1,3],0,"abc")
    notspecialcharacter='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789'
    for j in range(1,np.shape(a)[1]):
        isstrenglength1_this_element[j]=int(len(this_element[j])==1)
        isspecialcharacter_this_element[j]=int(not(this_element[j] in notspecialcharacter))
        output[j,1]=a[j,1]
        output[j,2]=a[j,2]
        output[j,3]=isstrenglength1_this_element[j]*isspecialcharacter[j]
    return output

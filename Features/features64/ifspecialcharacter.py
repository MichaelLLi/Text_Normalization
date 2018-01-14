#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:36:53 2017

@author: timschutzlkord, checked
"""

import numpy as np
 
def ifspecialcharacter(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],3))
    next_element=np.append(a[1:,2],"abc")
    this_element=a[:,2]
    previous_element=np.insert(a[:-1,2],0,"abc")
    notspecialcharacter='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789,.!? :;\'\"'
    for j in range(np.shape(a)[0]):         
        output[j,0]=int(len(str(next_element[j]))==1&(str(next_element[j])[0] not in notspecialcharacter))
        output[j,1]=int(len(str(this_element[j]))==1&(str(this_element[j])[0] not in notspecialcharacter))
        output[j,2]=int(len(str(previous_element[j]))==1&(str(previous_element[j])[0] not in notspecialcharacter))
    return output

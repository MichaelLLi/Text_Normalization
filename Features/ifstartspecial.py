# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 13:22:28 2017

@author: Michael
"""

from nltk.corpus import wordnet as wn
import numpy as np
def ifstartspecial(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],9))
    this_element=a[:,2]
    for i in range(np.shape(a)[0]):
        output[i,3]=int(this_element[i].startswith('#'))
        if '/' in this_element[i]:
            output[i,4]=1
        else:
            output[i,4]=0
        if '-' in this_element[i]:
            output[i,5]=1
        else:
            output[i,5]=0

    output[:,0]=np.append(output[:,3][1:],0)
    output[:,1]=np.append(output[:,4][1:],0)
    output[:,2]=np.append(output[:,5][1:],0)
    output[:,6]=np.insert(output[:,3][:-1],0,0)
    output[:,7]=np.insert(output[:,4][:-1],0,0)
    output[:,8]=np.insert(output[:,5][:-1],0,0)
    return output
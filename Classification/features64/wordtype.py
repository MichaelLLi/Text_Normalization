# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 12:02:28 2017

@author: Michael
"""
from nltk.corpus import wordnet as wn
import numpy as np
def wordtype(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],3))
    next_element=np.append(a[1:,2],'def')
    this_element=a[:,2]
    previous_element=np.insert(a[:-1,2],0,'def')
    for i in range(np.shape(a)[0]):
        if wn.synsets(str(this_element[i])):
            if wn.synsets(str(this_element[i]))[0].pos()=='n':
                output[i,1]=1
            elif wn.synsets(str(this_element[i]))[0].pos()=='v':
                output[i,1]=2
            elif wn.synsets(str(this_element[i]))[0].pos()=='a':
                output[i,1]=3
            elif wn.synsets(str(this_element[i]))[0].pos()=='s':
                output[i,1]=4
            elif wn.synsets(str(this_element[i]))[0].pos()=='r':
                output[i,1]=5
            else:
                output[i,1]=6
        else:
            output[i,1]=0
    output[:,0]=np.append(output[:,1][1:],0)
    output[:,2]=np.insert(output[:,1][:-1],0,0)    
    return output
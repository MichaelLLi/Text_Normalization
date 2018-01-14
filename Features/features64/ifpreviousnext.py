# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:52:59 2017

@author: Michael
"""
import numpy as np
def ifpreviousnext(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],2))
    sentence_ID=a[:,0]
    for j in range(np.shape(a)[0]):
        if j==0:
            output[j,0]=0
            if sentence_ID[j+1]==sentence_ID[j]:
                output[j,1]=1
            else:
                output[j,1]=0
        elif j==np.shape(a)[0]-1:
            output[j,1]=0
            if sentence_ID[j-1]==sentence_ID[j]:
                output[j,0]=1
            else:
                output[j,0]=0  
        else:
            if sentence_ID[j-1]==sentence_ID[j]:
                output[j,0]=1
            else:
                output[j,0]=0
            if sentence_ID[j+1]==sentence_ID[j]:
                output[j,1]=1
            else:
                output[j,1]=0
    return output
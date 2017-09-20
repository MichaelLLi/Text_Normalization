# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:52:59 2017

@author: Michael
"""
import numpy as np
def ifpreviousnext(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.array(shape=(np.shape(a)[1],2))
    sentence_ID=a[:,1]
    for j in range(np.shape(a)[1]):
        if j==1:
            output[j,1]=0
            if sentence_ID[j+1]==sentence_ID[j]:
                output[j,2]=1
            else:
                output[j,2]=0
        elif j==np.shape[1]-1:
            output[j,2]=0
            if sentence_ID[j-1]==sentence_ID[j]:
                output[j,1]=1
            else:
                output[j,1]=0  
        else:
            if sentence_ID[j-1]==sentence_ID[j]:
                output[j,1]=1
            else:
                output[j,1]=0
            if sentence_ID[j+1]==sentence_ID[j]:
                output[j,2]=1
            else:
                output[j,2]=0
    return output
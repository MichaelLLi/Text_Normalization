# -*- coding: utf-8 -*-
from collections import Counter
import numpy as np

def ifcountletters(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.array(shape=(np.shape[1],24))
    next_element=np.append(a[1:,3],"abc")
    this_element=a[:,3]
    previous_element=np.insert(a[:-1,3],0,"abc")
    letters=np.array(['aA','eE','iI','oO','uU',"aAeEiIoOuU","qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"])
    for i in range(1,7):
        for j in range(1,np.shape[1]):
            cnt1=Counter(previous_element[j])
            cnt2=Counter(this_element[j])
            cnt3=Counter(next_element[j])
            output[j,3*i-2]=sum(cnt1[x] for x in letters[i])
            output[j,3*i-1]=sum(cnt2[x] for x in letters[i])
            output[j,3*i]=sum(cnt3[x] for x in letters[i])  
    output[j,22]=output[j,19]-output[j,16]
    output[j,23]=output[j,20]-output[j,17]
    output[j,24]=output[j,21]-output[j,18]
    return output

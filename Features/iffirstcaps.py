# -*- coding: utf-8 -*-
from collections import Counter
import numpy as np
def step(x):
    return 1 * (x > 0)
def iffirstcaps(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.array(shape=(np.shape(a)[1],3))
    next_element=np.append(a[1:,3],"abc")
    this_element=a[:,3]
    previous_element=np.insert(a[:-1,3],0,"abc")
    next_element=next_element.astype('|S1')
    this_element=this_element.astype('|S1')
    previous_element=previous_element.astype('|S1')
    letters=np.array(['QWERTYUIOPASDFGHJKLZXCVBNM'])
    for j in range(1,np.shape(a)[1]):
        cnt1=Counter(previous_element[j])
        cnt2=Counter(this_element[j])
        cnt3=Counter(next_element[j])
        output[j,1]=step(sum(cnt1[x] for x in letters))
        output[j,2]=step(sum(cnt2[x] for x in letters))
        output[j,3]=step(sum(cnt3[x] for x in letters))
    return output
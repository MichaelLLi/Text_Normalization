# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
def __step(x):
    return 1 * (x > 0)
def iffirstcaps(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],6))
    next_element=np.append(a[1:,2],"abc")
    this_element=a[:,2]
    previous_element=np.insert(a[:-1,2],0,"abc")
    for j in range(np.shape(a)[0]):
        nxt=str(next_element[j])[0]
        ths=str(this_element[j])[0]
        prev=str(previous_element[j])[0]
        output[j,0]=int(nxt.isupper())
        output[j,1]=int(ths.isupper())
        output[j,2]=int(prev.isupper())
        if ths=='#':
            output[j,4]=1
    output[:,3]=np.append(output[:,4][1:],0)
    output[:,5]=np.insert(output[:,4][:-1],0,0)
    return output

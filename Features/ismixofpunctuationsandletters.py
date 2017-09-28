#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:16:10 2017

@author: timschutzlkord, based on Michael's script.
"""

import numpy as np
import pandas as pd
test = pd.read_csv('en_train_lim.csv')

 
def ismixofpunctuationsandletters(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],3))
    next_element=np.append(a[1:,2],"abc")
    this_element=a[:,2]
    previous_element=np.insert(a[:-1,2],0,"abc")
    punctuationsandletters=np.array([',.-_()+!? :;[]\'\"/','QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'])
    for j in range(1,np.shape(a)[1]+1):
        countpunctuations=0
        countletters=0
        for k in range(1,len(str(this_element[j-1]))+1):
            if str(this_element[j-1])[k-1] in punctuationsandletters[0]:
                countpunctuations=countpunctuations+1
            if str(this_element[j-1])[k-1] in punctuationsandletters[1]:
                countletters=countletters+1
        output[j-1,0]=a[j-1,0]
        output[j-1,1]=a[j-1,1]
        if (countpunctuations+countletters==len(str(this_element[j-1])))&(countpunctuations<len(str(this_element[j-1])))&(countletters<len(str(this_element[j-1]))):
            output[j-1,2]=1
        else:
            output[j-1,2]=0
    return output
    
test=test.values
output=ismixoflettersandspecialcharacters(test)
output
output1 = pd.DataFrame(output)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 17:35:51 2017

@author: timschutzlkord
"""

from collections import Counter
import numpy as np
import pandas as pd
test = pd.read_csv('en_train.csv')

def ifuppercaselettersanddots(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],3))
    next_element=np.append(a[1:,2],"abc")
    this_element=a[:,2]
    previous_element=np.insert(a[:-1,2],0,"abc")
    uppercaseletters='QWERTYUIOPASDFGHJKLZXCVBNM'
    dot='.'
    for j in range(np.shape(a)[0]):
        cnt_next = Counter(str(next_element[j]))
        cnt_this = Counter(str(this_element[j]))
        cnt_prev = Counter(str(previous_element[j]))
        output[j,0]=int((sum(cnt_next[x] for x in uppercaseletters) + sum(cnt_next[x] for x in dot) == len(str(next_element[j]))) & (sum(cnt_next[x] for x in uppercaseletters) >= 1) & (sum(cnt_next[x] for x in dot) >= 1))
        output[j,1]=int((sum(cnt_this[x] for x in uppercaseletters) + sum(cnt_this[x] for x in dot) == len(str(this_element[j]))) & (sum(cnt_this[x] for x in uppercaseletters) >= 1) & (sum(cnt_this[x] for x in dot) >= 1))
        output[j,2]=int((sum(cnt_prev[x] for x in uppercaseletters) + sum(cnt_prev[x] for x in dot) == len(str(previous_element[j]))) & (sum(cnt_prev[x] for x in uppercaseletters) >= 1) & (sum(cnt_prev[x] for x in dot) >= 1))
    return output
    
test1=test.values[:,[0,1,3]]
output=ifuppercaselettersanddots(test1)
output1 = pd.DataFrame(output)
output1.columns = ['if_next_upper_case_letters_and_dots','if_this_upper_case_letters_and_dots','if_prev_upper_case_letters_and_dots']
output1.to_csv('output_train_26.csv')
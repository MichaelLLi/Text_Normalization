# -*- coding: utf-8 -*-
import numpy as np
import enchant
def ifusenglishword(a):
    # accept input argument as numpy array of n rows and 3 columns
    d=enchant.Dict("en_US")
    output=np.array(shape=(np.shape(a)[1],3))
    next_element=np.append(a[1:,3],"abc")
    this_element=a[:,3]
    previous_element=np.insert(a[:-1,3],0,"abc")
    output[:,1]=d.check(previous_element)
    output[:,2]=d.check(this_element)
    output[:,3]=d.check(next_element)
    return output

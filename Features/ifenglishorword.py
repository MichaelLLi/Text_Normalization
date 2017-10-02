# -*- coding: utf-8 -*-
import numpy as np
import enchant
def ifenglishorword(a):
    # accept input argument as numpy array of n rows and 3 columns
    d,e,f=enchant.Dict("en_US"), enchant.Dict("en_GB"), enchant.Dict("en_AU")
    output=np.zeros(shape=(np.shape(a)[0],6))
    next_element=np.append(a[1:,2],'abc')
    this_element=a[:,2]
    previous_element=np.insert(a[:-1,2],0,'abc')
    g,h=enchant.Dict("de_DE"), enchant.Dict("fr_FR")
    for i in range(np.shape(a)[0]):
        output[i,0]=np.logical_or(f.check(previous_element[i]),np.logical_or(d.check(previous_element[i]), e.check(previous_element[i])))
        output[i,1]=np.logical_or(f.check(this_element[i]),np.logical_or(d.check(this_element[i]), e.check(this_element[i])))
        output[i,2]=np.logical_or(f.check(next_element[i]),np.logical_or(d.check(next_element[i]), e.check(next_element[i])))
        output[i,3]=np.logical_or(output[i,0],np.logical_or(g.check(previous_element[i]), h.check(previous_element[i])))
        output[i,4]=np.logical_or(output[i,1],np.logical_or(g.check(this_element[i]), h.check(this_element[i])))
        output[i,5]=np.logical_or(output[i,2],np.logical_or(g.check(next_element[i]), h.check(next_element[i])))    
    return output





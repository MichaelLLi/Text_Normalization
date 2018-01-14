# -*- coding: utf-8 -*-
import numpy as np
import enchant
def ifenglishorword(a):
    # accept input argument as numpy array of n rows and 3 columns
    d,e,f=enchant.Dict("en_US"), enchant.Dict("en_GB"), enchant.Dict("en_AU")
    output=np.zeros(shape=(np.shape(a)[0],9))
    next_element=np.append(a[1:,2],'abc')
    this_element=a[:,2]
    previous_element=np.insert(a[:-1,2],0,'abc')
    g,h=enchant.Dict("de_DE"), enchant.Dict("fr_FR")
    for i in range(np.shape(a)[0]):
        output[i,0]=np.logical_or(f.check(str(previous_element[i])),np.logical_or(d.check(str(previous_element[i])), e.check(str(previous_element[i]))))
        output[i,1]=np.logical_or(f.check(str(this_element[i])),np.logical_or(d.check(str(this_element[i])), e.check(str(this_element[i]))))
        output[i,2]=np.logical_or(f.check(str(next_element[i])),np.logical_or(d.check(str(next_element[i])), e.check(str(next_element[i]))))
        output[i,3]=np.logical_or(output[i,0],np.logical_or(g.check(str(previous_element[i])), h.check(str(previous_element[i]))))
        output[i,4]=np.logical_or(output[i,1],np.logical_or(g.check(str(this_element[i])), h.check(str(this_element[i]))))
        output[i,5]=np.logical_or(output[i,2],np.logical_or(g.check(str(next_element[i])), h.check(str(next_element[i]))))
        output[i,6]=d.check(str(previous_element[i]))
        output[i,7]=d.check(str(this_element[i]))
        output[i,8]=d.check(str(next_element[i]))
    return output





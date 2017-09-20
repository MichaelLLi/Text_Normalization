# -*- coding: utf-8 -*-
import numpy as np
import enchant
def ifenglishorword(a):
    # accept input argument as numpy array of n rows and 3 columns
    d,e,f=enchant.Dict("en_US"), enchant.Dict("en_GB"), enchant.Dict("en_AU")
    output=np.array(shape=(np.shape(a)[1],6))
    next_element=np.append(a[1:,3],"abc")
    this_element=a[:,3]
    previous_element=np.insert(a[:-1,3],0,"abc")
    g,h=enchant.Dict("de_DE"), enchant.Dict("fr_FR")
    output[:,1]=np.logical_or(f.check(previous_element),np.logical_or(d.check(previous_element), e.check(previous_element)))
    output[:,2]=np.logical_or(f.check(this_element),np.logical_or(d.check(this_element), e.check(this_element)))
    output[:,3]=np.logical_or(f.check(next_element),np.logical_or(d.check(next_element), e.check(next_element)))
    output[:,4]=np.logical_or(output[:,1],np.logical_or(g.check(previous_element), h.check(previous_element)))
    output[:,5]=np.logical_or(output[:,2],np.logical_or(g.check(this_element), h.check(this_element)))
    output[:,6]=np.logical_or(output[:,3],np.logical_or(g.check(next_element), h.check(next_element)))    
    return output





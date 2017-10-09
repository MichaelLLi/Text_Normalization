#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 13:07:09 2017

@author: timschutzlkord
"""
def ifwebsite(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],3))
    next_element=np.append(a[1:,2],"abc")
    this_element=a[:,2]
    previous_element=np.insert(a[:-1,2],0,"abc")
    dot='.'
    space=' '
    letters='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    capitals='QWERTYUIOPASDFGHJKLZXCVBNM'
    numbers='0123456789'
    for j in range(1,np.shape(a)[0]+1):
        countdot = 0
        countdotsub = 0
        identifier = 0
        countspace = 0
        countnumber = 0
        # identifierdotstart = 0
        identifierdotend = 0
        # Pattern .sth
        # if(str(this_element[j-1])[0] in dot)&(len(str(this_element[j-1]))!=1):
            # identifier = 1
        if(str(this_element[j-1])[len(str(this_element[j-1]))-1] in dot)&(len(str(this_element[j-1]))!=1):
            identifierdotend = 1
        # Pattern Num.Num
        for k in range(2,len(str(this_element[j-1]))):
            # if(str(this_element[j-1])[k-2] in numbers)&(str(this_element[j-1])[k-1] in dot)&((str(this_element[j-1])[k] in numbers)):
                # countdot = countdot + 1
                # Countdot need to be greater than 1
            if(str(this_element[j-1])[k-2] in letters)&(str(this_element[j-1])[k-1] in dot)&((str(this_element[j-1])[k] in letters)):
                identifier = 1
            if(str(this_element[j-1])[0] not in dot)&(str(this_element[j-1])[k-2] in numbers)&(str(this_element[j-1])[k-1] in dot)&((str(this_element[j-1])[k] in letters)):
                identifier = 1
        for k in range(1,len(str(this_element[j-1]))+1):
            if(str(this_element[j-1])[k-1] in space):
                countspace = countspace + 1
            if(str(this_element[j-1])[k-1] in dot):
                countdotsub = countdotsub + 1
            if(str(this_element[j-1])[k-1] in numbers):
                countnumber = countnumber + 1
        # if(countnumber + countdotsub == len(str(this_element[j-1]))):
        if(countnumber + countdotsub == len(str(this_element[j-1]))):
            if(countdotsub == 3):
                identifier = 1
            else:
                identifier = 0
        # Avoid Pattern ".6"
        if(((str(this_element[j-1])[len(str(this_element[j-1]))-2]=='\'')&(str(this_element[j-1])[len(str(this_element[j-1]))-1]=='s')))|(((str(this_element[j-1])[len(str(this_element[j-1]))-2]=='.')&(str(this_element[j-1])[len(str(this_element[j-1]))-1] in letters))):
            identifier = 0
        if((str(this_element[j-1])[0:5]=='http:')|(str(this_element[j-1])[0:6]=='https:')|(str(this_element[j-1])[0:4]=='www.')):
            identifier = 1            
        if(identifier==1)&(countspace==0)&(identifierdotend==0):
            output[j-1,1]=1
        else:
            output[j-1,1]=0
    for l in range(2,np.shape(a)[0]+1):
        output[l-1,2]=output[l-2,1]
    for m in range(1,np.shape(a)[0]):
        output[m-1,0]=output[m,1]
    return output

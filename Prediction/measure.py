import re
from num2words import num2words
import numpy as np
import pandas as pd

def measure(a):
    # output= np.empty(shape=(len(a),1),dtype=object)
    output=['AAAis is wrong!'] * len(a)
    data=pd.read_csv("measure_trans.csv")
    datam=data.as_matrix()
    inputx=datam[:,1]
    outputx=datam[:,2]
    for i in range(len(a)):
        try:
            word=str(a[i])
            word=word.replace(",","")
            if "-" in word:
                output_temp="minus "
            else:
                output_temp=""
            comp=re.findall(r'[0-9.]+|[A-Za-zµ/%\u0374-\u03FF\'\"]+[ /A-Za-z0-9⁰¹²³⁴⁵⁶⁷⁸⁹]?', word)
            if len(comp)>0:
                for k in range(len(comp)):
                    comp[k]=comp[k].replace(" ","")
                try:
                    num_temp=decimal([comp[0]])[0][0]
                    output_temp+=num_temp
                    if len(comp)>1:
                        for j in range(1, len(comp)):
                            if comp[j] in inputx:
                                k=np.where(inputx==comp[j])
                                index=k[0][0]
                                output_temp += " " + outputx[index]
                    if float(comp[0])==1 and output_temp[-1]=="s":
                        output_temp=output_temp[:-1]
                except ValueError:
                    output_temp=""
                    for j in range(len(comp)):
                        if comp[j] in inputx:
                            k=np.where(inputx==comp[j])
                            index=k[0][0]
                            if j>0:
                                output_temp +=" "
                            output_temp += outputx[index]
                    if len(output_temp)>0:
                        if output_temp[-1]=="s":
                            output_temp=output_temp[:-1]
                output_temp=re.sub( '\s+', ' ', output_temp)
            output[i]=output_temp
        except ValueError:
            output[i]='AAAis is wrong!'
        except TypeError:
            output[i]='AAAis is wrong!'
    return output

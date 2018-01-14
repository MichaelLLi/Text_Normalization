import re
from num2words import num2words
import numpy as np
import pandas as pd

def money(a):
    # output= np.empty(shape=(len(a),1),dtype=object)
    output=['AAAis is wrong!'] * len(a)
    money=pd.read_csv("money_trans.csv")
    money=money.as_matrix()
    inputx=money[:,1]
    outputx=money[:,2]
    for i in range(len(a)):
        try:
            word=str(a[i])
            dec_comp=re.sub("[^0-9.]+","",word)
            match_comp=re.sub("[0-9,.]+","",word)
            match_comp=match_comp.strip()
            try:
                if round(float(dec_comp))==float(dec_comp):
                    output_temp=decimal([str(round(float(dec_comp)))])[0][0]
                else:
                    output_temp=decimal([dec_comp])[0][0]
            except ValueError:
                output_temp=decimal([dec_comp])[0][0]
            if match_comp in inputx:
                k=np.where(inputx==match_comp)
                index=k[0][0]
                output_temp += " "
                output_temp +=outputx[index]
            try:
                if float(dec_comp.replace(",",""))==1 and output_temp[-1]=="s" and "million" not in output_temp and "billion" not in output_temp and "thousand" not in output_temp:
                    output_temp=output_temp[:-1]
            except ValueError:
                output_temp=output_temp
            
            output[i]=output_temp
        except ValueError:
            output[i]='AAAis is wrong!'
        except TypeError:
            output[i]='AAAis is wrong!'
    return output    

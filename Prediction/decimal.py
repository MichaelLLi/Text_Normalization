import re
from num2words import num2words
import numpy as np
import pandas as pd

def decimal(a):
    output= np.empty(shape=(len(a),1),dtype=object)
    for i in range(len(a)):
        try:
            word=str(a[i])
            if "-" in word:
                output_temp="minus "
            else:
                output_temp=""
            suffix=re.findall(r'[Aa-zZ]+',word)
            word=re.sub("[^0-9.]","",word)
            comp=re.findall(r'[0-9]+|[0-9.]+',word)   
            if len(comp)==2:
                num_temp=num2words(int(comp[0]))
                num_temp=num_temp.replace(" and "," ")
                num_temp=num_temp.replace("-"," ")
                num_temp=num_temp.replace(",","")
                output_temp += num_temp
                decimal_temp=comp[1].replace(".","")
                output_temp += " point"
                for char in decimal_temp:
                    if (int(char)==0 and len(decimal_temp)>1) or (int(char)==0 and len(decimal_temp)==1 and suffix):
                        output_temp += " o"
                    elif int(char)==0 and len(decimal_temp)==1 and not suffix:
                        output_temp += " zero"
                    else:
                        output_temp += " "
                        output_temp += num2words(int(char))
            elif len(comp)==1:
                if "." in comp[0]:
                    output_temp +="point"
                    decimal_temp=comp[0].replace(".","")
                    for char in decimal_temp:
                        if int(char)==0:
                            output_temp += " o"
                        else:
                            output_temp += " "
                            output_temp += num2words(int(char))
                else:
                    num_temp=num2words(int(comp[0]))
                    num_temp=num_temp.replace(" and "," ")
                    num_temp=num_temp.replace("-"," ")
                    num_temp=num_temp.replace(",","")
                    output_temp += num_temp
            if suffix:
                output_temp += " "
                output_temp += suffix[0]
            output[i]=output_temp
        except ValueError:
            output[i]='AAAis is wrong!'
        except TypeError:
            output[i]='AAAis is wrong!'
    return output

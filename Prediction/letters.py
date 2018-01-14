import numpy as np
import re

def letters(a):
    output= np.empty(shape=(len(a),1),dtype=object)
    capture=pd.read_csv("letter_capture.csv")
    capture=capture.values
    capture_set=set(capture[:,1])
    for i in range(len(a)):
        if str(a[i]).lower() in capture_set:
            output_temp=str(a[i])
        else:
            if '\'s' in str(a[i]):
                temp0=str(a[i]).replace('\'s', '')
                if 'é' in temp0:
                    loc=temp0.find("é")
                    temp1=temp0[:loc]
                    temp2=temp0[(loc+1):]
                    regex = re.compile('[^a-zA-Z&]')
                    temp1=regex.sub('', temp1)
                    temp1=temp1.lower()
                    temp1=temp1.replace('', ' ')[1: -1]
                    temp2=regex.sub('', temp2)
                    temp2=temp2.lower()
                    temp2=temp2.replace('', ' ')[1: -1] + '\'s'
                    output_temp=temp1.replace('&','and') + " e acute " +temp2.replace('&','and')              
                else:
                    regex = re.compile('[^a-zA-Z&]')
                    temp0=regex.sub('', temp0)
                    temp=temp0.lower()
                    temp=temp.replace('', ' ')[1: -1] + '\'s'
                    output_temp=temp.replace('&','and')
            else:
                if 'é' in str(a[i]):
                    loc=str(a[i]).find("é")
                    temp1=str(a[i])[:loc]
                    temp2=str(a[i])[(loc+1):]
                    regex = re.compile('[^a-zA-Z&]')
                    temp1=regex.sub('', temp1)
                    temp1=temp1.lower()
                    temp1=temp1.replace('', ' ')[1: -1]
                    temp2=regex.sub('', temp2)
                    temp2=temp2.lower()
                    temp2=temp2.replace('', ' ')[1: -1]
                    output_temp=temp1.replace('&','and') + " e acute " +temp2.replace('&','and')                     
                else:
                    regex = re.compile('[^a-zA-Z&]')
                    temp0=regex.sub('', str(a[i]))
                    temp=temp0.lower()
                    temp=temp.replace('', ' ')[1: -1]
                    output_temp=temp.replace('&','and')
            if str(a[i]).isupper() and len(str(a[i]))==1:
                output_temp=output_temp.upper()
            else:
                output_temp=output_temp
            if str(a[i])[-1]=="s" and '\'s' not in str(a[i]) and str(a[i]).lower()!=str(a[i]):
                output_temp=output_temp[:-1].strip()+"'s"
            output_temp=output_temp.strip()
        output[i]=output_temp
    return output

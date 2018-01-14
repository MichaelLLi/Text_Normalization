import re
from num2words import num2words
import numpy as np

def digit(a):
    # output= np.empty(shape=(len(a),1),dtype=object)
    output=['AAAis is wrong!'] * len(a)
    for i in range(len(a)):
        try:
            word=str(a[i])
            word=re.sub('[^0-9]+', '', word)
            output_temp=""
            counter=0
            for char in word:
                if int(char)==0:
                    if counter !=0:
                        output_temp +=" "
                    output_temp += "o"
                    counter +=1
                else:
                    if counter !=0:
                        output_temp +=" "
                    output_temp += num2words(int(char))
                    counter +=1
            output[i]=output_temp
        except ValueError:
            output[i]='AAAis is wrong!'
        except TypeError:
            output[i]='AAAis is wrong!'
    return output 

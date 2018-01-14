from num2words import num2words
import numpy as np
alpha="qwertyuiopasdfghjklzxcvbnm"

def telephone(a):
    # output= np.empty(shape=(len(a),1),dtype=object)
    output=['AAAis is wrong!'] * len(a)
    for i in range(len(a)):
        try:
            temp=""
            counter=0
            for char in str(a[i]).lower():
                try:
                    if counter !=0 and int(char)>=0:
                        temp += " "
                    if int(char)==0:
                        temp += "o"
                        counter +=1
                    else:
                        temp += num2words(int(char))
                        counter +=1
                except ValueError:
                    if char in alpha:
                        if counter !=0:
                            temp += " "
                        temp += char
                        counter +=1
                    elif counter!=0:
                        temp +=" "
                        temp += "sil"
                        counter +=1
                except OverflowError:
                    if char in alpha:
                        if counter !=0:
                            temp += " "
                        temp += char
                        counter +=1
                    elif counter!=0:
                        temp +=" "
                        temp += "sil"
                        counter +=1
            output[i]=temp
        except ValueError:
            output[i]='AAAis is wrong!'
        except TypeError:
            output[i]='AAAis is wrong!'
    return output

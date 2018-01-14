from collections import Counter
from num2words import num2words
import numpy as np
import pandas as pd
import re

letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
numbers = '0123456789'

def address(a):
    output=[None] * len(a)
    inputaddress=a
    for j in range(len(a)):
        inputaddress[j] = re.sub('[- \.,]','',str(inputaddress[j]))
        cnt = Counter(str(inputaddress[j]))
        sum_l = sum(cnt[x] for x in letters)
        sum_n = sum(cnt[x] for x in numbers)
        l, n = inputaddress[j][:sum_l], inputaddress[j][sum_l:]
        l = l.lower()
        if sum_l >=3 :
            l = ''.join(l)
        else:
            l = ' '.join(l)
        if (l == 'u s') & (sum_n > 3) :
            if sum_n == 4:
                n = num2words(int(str(n[:2]))) + ' ' +  num2words(int(str(n[2:])))
            else:
                n = num2words(int(str(n)))
        else: 
            if sum_n == 1:
                n = num2words(int(str(n)))
            elif sum_n == 2:
                cnt_n = Counter(str(n))
                sum_nn = sum(cnt_n[x] for x in letters)
                if sum_nn == 0:
                    if str(n[0]) == '0':
                        n = 'o' + ' ' + num2words(int(str(n[1])))
                    else:
                        n = num2words(int(str(n)))
            elif sum_n == 3:
                cnt_nn = Counter(str(n))
                sum_nnn = sum(cnt_nn[x] for x in letters)
                if sum_nn == 0:
                    if (str(n[0]) == '0')&(str(n[1]) == '0'):
                        n = 'o' + ' ' + 'o' + ' ' + num2words(int(str(n)[2]))
                    elif (str(n[0]) == '0')&(str(n[1]) != '0'):
                        n = num2words(int(str(n)[1:]))
                    else:
                        if (str(n[1]) == '0'):
                            n = num2words(int(str(n)[0])) + ' '+'o' + ' ' + num2words(int(str(n)[2]))
                        else: 
                            n1, n2 = n[0], n[1:]
                            n1 = num2words(int(str(n1)))
                            n2 = num2words(int(str(n2)))
                            n = n1 + ' ' + n2
            else:
                n = ' '.join(n)
                n = re.sub('0','o',n)
                n = re.sub('1','one',n)
                n = re.sub('2','two',n)
                n = re.sub('3','three',n)
                n = re.sub('4','four',n)
                n = re.sub('5','five',n)
                n = re.sub('6','six',n)
                n = re.sub('7','seven',n)
                n = re.sub('8','eight',n)
                n = re.sub('9','nine',n)
        output[j] = l + ' ' + n
        output[j] = re.sub('-',' ',output[j])
        output[j] = re.sub('zero','o',output[j])
        output[j] = re.sub(' and','',output[j])
        output[j] = re.sub(',','',output[j])
    return output

from collections import Counter
from num2words import num2words
import numpy as np
import pandas as pd
import re

letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
numbers = '0123456789'

def dateyear(a):
    if isinteger(str(a)):
        a = int(a)
        if ((a/100).is_integer()) & ((a/1000).is_integer()) & (a >= 100):
            o = num2words(int(str(a)[:-3])) + ' ' + 'thousand'
            o = re.sub(' and','',o)
            return o
        elif ((a/100).is_integer()) & ((a/1000).is_integer() == False) & (a >= 100): 
            o = num2words(int(str(a)[:-2])) + ' ' + 'hundred'
            o = re.sub(' and','',o)
            return o
        else:
            if (int(a) >= 2000) & (int(a) <= 2009):
                o = num2words(int(str(a)))
                o = re.sub(' and','',o)
                return o
            elif len(str(a)) == 4:
                if str(a)[2] == '0': 
                    o = num2words(int(str(a)[:2])) + ' ' + 'o' + ' ' + num2words(int(str(a)[3:]))
                    o = re.sub(' and','',o)
                    o = re.sub('-',' ',o)
                    return o
                else: 
                    o = num2words(int(str(a)[:2])) + ' ' + num2words(int(str(a)[2:]))
                    o = re.sub(' and','',o)
                    o = re.sub('-',' ',o)
                    return o
            elif len(str(a)) == 3:
                if str(a)[1] == '0': 
                    o = num2words(int(str(a)[:1])) + ' ' + 'o' + ' ' + num2words(int(str(a)[2:]))
                    o = re.sub(' and','',o)
                    o = re.sub('-',' ',o)
                    return o
                else: 
                    o = num2words(int(str(a)[:1])) + ' ' + num2words(int(str(a)[1:]))
                    o = re.sub(' and','',o)
                    o = re.sub('-',' ',o)
                    return o
            elif (len(str(a)) == 2) | (len(str(a)) == 1):
                o = num2words(int(str(a)))
                o = re.sub(' and','',o)
                o = re.sub('-',' ',o)
                return o
    else:       
        return a
    
def address(a):
    output=[0] * len(a)
    inputaddress=a
    space = ' '
    for j in range(len(a)):
        try:
            inputaddress[j] = re.sub('[.,]','', inputaddress[j])
            inputaddress[j] = re.sub('[-]',' ', inputaddress[j])
            cnt = Counter(inputaddress[j])
            cnt_space = sum(cnt[x] for x in space)
            orientation = {'e':'east','w': 'west', 'n': 'north', 's' : 'south', 'ne' : 'northeast', 'se' : 'southeast', 'nw' : 'northwest', 'sw' : 'southwest', 'us':'us'}      
            seg = re.findall(r"[a-zA-Z]+|[0-9]+",str(inputaddress[j]))
            # if cnt_space == 0:
            seg[0] = str(seg[0]).lower()        
            if len(seg[0]) >= 4:
                seg[0] = ''.join(seg[0])
            else:
                seg[0] = ' '.join(seg[0])
            if len(seg) == 3:
                seg[2] = str(seg[2]).lower()  
                if str(seg[2]) in orientation:
                    if len(str(seg[1])) >= 3:
                        output[j] = str(seg[0]) + ' ' + dateyear(int(str(seg[1]))) + ' ' + orientation[str(seg[2]).lower()]
                        output[j] = re.sub('-',' ',output[j])
                    else: 
                        output[j] = str(seg[0]) + ' ' + num2words(int(str(seg[1]))) + ' ' + orientation[str(seg[2]).lower()]
                        output[j] = re.sub('-',' ',output[j])
                else:
                    output[j] = str(seg[0]) + ' ' + num2words(int(str(seg[1]))) + ' ' + str(seg[2])
                    output[j] = re.sub('-',' ',output[j])
            elif (cnt_space == 0) & (len(seg[1]) == 1):
                n = ' '.join(seg[1])
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
                output[j] = str(seg[0]) + ' ' + n
                
            elif (cnt_space == 0) & (len(seg[1]) == 2):
                if seg[1][0] != '0':
                    output[j] = str(seg[0]) + ' ' + num2words(int(str(seg[1])))
                    output[j] = re.sub('zero','o',output[j]) 
                    output[j] = re.sub('-',' ',output[j])
                else: 
                    output[j] = str(seg[0]) + ' ' + 'o' + ' ' + num2words(int(str(seg[1])[-1]))
                    output[j] = re.sub('zero','o',output[j]) 
                    output[j] = re.sub('-',' ',output[j])
            elif (cnt_space == 0) & (len(seg[1]) == 3):
                if str(seg[1])[-2:] == '00':
                    output[j] = str(seg[0]) + ' ' + num2words(int(str(seg[1])[0]))+ ' ' + 'hundred'
                elif str(seg[1])[:2] == '00':
                    output[j] = str(seg[0]) + ' o o ' + num2words(int(str(seg[1])[1:]))
                    output[j] = re.sub('-',' ',output[j])
                elif str(seg[1])[0] == '0':
                    output[j] = str(seg[0]) + ' ' + num2words(int(str(seg[1])[1:]))
                    output[j] = re.sub('-',' ',output[j])
                elif (seg[1][-1] != '0'): 
                    n = ' '.join(seg[1])
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
                    output[j] = str(seg[0]) + ' ' + n
                else:
                    output[j] = str(seg[0]) + ' ' + dateyear(seg[1])
                    output[j] = re.sub('-',' ',output[j]) 
            elif (cnt_space == 0) & (len(seg[1]) == 4):
                if str(seg[1])[-3:] == '000':
                    output[j] = str(seg[0]) + ' ' + num2words(int(str(seg[1])[0]))+ ' ' + 'thousand'
                elif str(seg[1])[-2:] == '00':
                    output[j] = str(seg[0]) + ' ' + num2words(int(str(seg[1])[:2]))+ ' ' + 'hundred'
                    output[j] = re.sub('-',' ',output[j])
                elif str(seg[1])[:3] == '000':
                    output[j] = str(seg[0]) + ' o o o ' + num2words(int(str(seg[1])[-1]))
                elif str(seg[1])[:2] == '00':
                    output[j] = str(seg[0]) + ' ' + num2words(int(str(seg[1])[-2:]))
                    output[j] = re.sub('-',' ',output[j])
                else:
                    n = ' '.join(seg[1])
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
                    output[j] = str(seg[0]) + ' ' + n
            elif (cnt_space == 0) & (len(seg[1]) >= 5):
                zeroseg = re.findall(r"[0]+|[0-9]+",seg[1])
                if len(zeroseg) == 2:
                    if len(zeroseg[1]) == 2:
                        output[j] = seg[0] + ' ' + num2words(int(str(zeroseg[1])))
                        output[j] = re.sub('-',' ',output[j])
                    elif len(zeroseg[1]) == 1:
                        n = ' '.join(seg[1])
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
                        output[j] = str(seg[0]) + ' ' + n
                    else:
                        n = ' '.join(seg[1])
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
                        output[j] = str(seg[0]) + ' ' + n
                else:
                    n = ' '.join(seg[1])
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
                    output[j] = str(seg[0]) + ' ' + n
            elif (cnt_space >= 1) & (len(seg[1]) <= 2): 
                output[j] = str(seg[0]) + ' ' + num2words(int(str(seg[1])))
                output[j] = re.sub('zero','o',output[j]) 
                output[j] = re.sub('-',' ',output[j])
            elif (cnt_space >= 1) & (len(seg[1]) == 3): 
                if str(seg[1])[-2:] == '00':
                    output[j] = str(seg[0]) + ' ' + num2words(int(str(seg[1])[0]))+ ' ' + 'hundred'
                elif str(seg[1])[:2] == '00':
                    output[j] = str(seg[0]) + ' o o ' + num2words(int(str(seg[1])[1:]))
                    output[j] = re.sub('-',' ',output[j])
                elif str(seg[1])[0] == '0':
                    output[j] = str(seg[0]) + ' ' + num2words(int(str(seg[1])[1:]))
                    output[j] = re.sub('-',' ',output[j])
                elif (str(seg[1])[0] != '0') & (str(seg[1])[1] != '0'):
                    output[j] = str(seg[0]) + ' ' + dateyear(str(seg[1]))
                    output[j] = re.sub('-',' ',output[j]) 
                elif (str(seg[1])[0] != '0') & (str(seg[1])[1] == '0'):
                    output[j] = str(seg[0]) + ' ' + num2words(int(str(seg[1][0]))) + ' ' + 'o' + ' ' + num2words(int(str(seg[1][-1])))
                else:
                    n = ' '.join(seg[1])
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
                    output[j] = str(seg[0]) + ' ' + n
            elif (cnt_space >= 1) & (len(seg[1]) == 4): 
                if str(seg[1])[-3:] == '000':
                    output[j] = str(seg[0]) + ' ' + num2words(int(str(seg[1])[0]))+ ' ' + 'thousand'
                elif str(seg[1])[-2:] == '00':
                    output[j] = str(seg[0]) + ' ' + num2words(int(str(seg[1])[:2]))+ ' ' + 'hundred'
                    output[j] = re.sub('-',' ',output[j])
                elif str(seg[1])[:3] == '000':
                    output[j] = str(seg[0]) + ' ' + num2words(int(str(seg[1])[-1]))
                elif str(seg[1])[:2] == '00':
                    output[j] = str(seg[0]) + ' ' + num2words(int(str(seg[1])[-2:]))
                    output[j] = re.sub('-',' ',output[j])
                elif (int(seg[1]) < 2100) & (seg[1][0] != '0'):
                    output[j] = str(seg[0]) + ' ' + dateyear(seg[1])
                else: 
                    n = ' '.join(seg[1])
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
                    output[j] = str(seg[0]) + ' ' + n  

            else:     
                output[j] = seg[0]
            if ((seg[0] == 'u s')| (seg[0] == 's r') | (seg[0] == 'c r') | (seg[0] == 'i')) & (len(str(seg[1])) > 4):
                output[j] = str(seg[0]) + ' ' + num2words(int(str(seg[1])))
                output[j] = re.sub('-',' ',output[j]) 
                output[j] = re.sub(',','',output[j]) 
            elif ((seg[0] == 'u s')| (seg[0] == 's r') | (seg[0] == 'c r') | (seg[0] == 'i')) & (len(str(seg[1])) <= 4) & (len(seg) <= 2):
                output[j] = str(seg[0]) + ' ' + dateyear(int(str(seg[1])))
                output[j] = re.sub('-',' ',output[j]) 
                output[j] = re.sub(',','',output[j])
            output[j] = re.sub(' and','',output[j]) 
        except ValueError:
            output[j]='AAAis is wrong!'
        except TypeError:
            output[j]='AAAis is wrong!'
        except IndexError:
            output[j]='AAAis is wrong!'
    return output

import re
from num2words import num2words
import numpy as np
import pandas as pd

def isinteger(a):
    try:
        int(a)
        return True
    except ValueError:
        return False

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
                if (str(a)[2] == '0') & (str(a)[1:3] != '00'): 
                    o = num2words(int(str(a)[:2])) + ' ' + 'o' + ' ' + num2words(int(str(a)[3:]))
                    o = re.sub(' and','',o)
                    o = re.sub('-',' ',o)
                    return o
                elif (str(a)[2] == '0') & (str(a)[1:3] == '00'):
                    o = num2words(int(str(a)))
                    o = re.sub(' and', '', o)
                    o = re.sub('-',' ',o)
                    return o
                else: 
                    o = num2words(int(str(a)[:2])) + ' ' + num2words(int(str(a)[2:]))
                    o = re.sub(' and','',o)
                    o = re.sub('-',' ',o)
                    return o
            elif len(str(a)) == 3:
                if str(a)[1] == '0': 
                    o = num2words(int(str(a)))
                    # o = num2words(int(str(a)[:1])) + ' ' + 'o' + ' ' + num2words(int(str(a)[2:]))
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
    
def ties(a):
    if isinteger(str(a)):
        a = int(a)
        if a == 10:
            return 'tens'
        elif a == 20:
            return 'twenties'
        elif a == 30:
            return 'thirties'
        elif a == 40:
            return 'forties'
        elif a == 50:
            return 'fifties'
        elif a == 60:
            return 'sixties'
        elif a == 70:
            return 'seventies'
        elif a == 80:
            return 'eighties'
        elif a == 90:
            return 'nineties'
        else:
            return a
    else:
        return a
    
def yearpluss(a):
    if isinteger(str(a)):
        # a = int(a)
        if ((int(a)/100).is_integer()) & ((int(a)/1000).is_integer()) & (int(a) >= 100):
            o = num2words(int(str(a)[:-3])) + ' ' + 'thousands'
            o = re.sub(' and','',o)
            return o
        elif ((int(a)/100).is_integer()) & ((int(a)/1000).is_integer() == False) & (int(a) >= 100): 
            o = num2words(int(str(a)[:-2])) + ' ' + 'hundreds'
            o = re.sub(' and','',o)
            return o
        elif ((int(a)/10).is_integer()) & ((int(a)/100).is_integer() == False) & ((int(a)/1000).is_integer() == False) & (int(a) >= 1): 
            if len(str(a)) >= 3 :
                o = num2words(int(str(a)[:-2])) + ' ' + str(ties(str(a)[-2:]))
                o = re.sub(' and','',o)
                return o
            elif len(str(a)) ==2:
                o = str(ties(int(str(a))))
                o = re.sub(' and','',o)
                return o
        else:
            if (int(a) >= 2000) & (int(a) <= 2009):
                if str(a)[-1] != '6':
                    o = num2words(int(str(a))) + 's'
                    o = re.sub(' and','',o)
                    return o
                else:
                    o = num2words(int(str(a))) + 'es'
                    o = re.sub(' and','',o)
                    return o
            elif len(str(a)) == 4:
                if str(a)[2] == '0': 
                    if (str(a)[-1] != '6'):
                        o = num2words(int(str(a)[:2])) + ' ' + 'o' + ' ' + num2words(int(str(a)[3:])) + 's'
                        o = re.sub(' and','',o)
                        o = re.sub('-',' ',o)
                        return o
                    elif (str(a)[-2:] == '16'):
                        o = num2words(int(str(a))) + 's'
                        o = re.sub(' and','',o)
                        o = re.sub('-',' ',o)
                        return o
                    else:
                        o = num2words(int(str(a)[:2])) + ' ' + 'o' + ' ' + num2words(int(str(a)[3:])) + 'es'
                        o = re.sub(' and','',o)
                        o = re.sub('-',' ',o)
                        return o
                else: 
                    if (str(a)[-1] != '6'):
                        o = num2words(int(str(a)[:2])) + ' ' + num2words(int(str(a)[2:])) + 's'
                        o = re.sub(' and','',o)
                        o = re.sub('-',' ',o)
                        return o
                    elif (str(a)[-2:] == '16'):
                        o = num2words(int(str(a))) + 's'
                        o = re.sub(' and','',o)
                        o = re.sub('-',' ',o)
                        return o
                    else:
                        o = num2words(int(str(a)[:2])) + ' ' + num2words(int(str(a)[2:])) + 'es'
                        o = re.sub(' and','',o)
                        o = re.sub('-',' ',o)
                        return o
            elif len(str(a)) == 3:
                if str(a)[1] == '0': 
                    if (str(a)[-1] != '6'):
                        o = num2words(int(str(a)[0])) + ' ' + 'hundred' + ' ' + num2words(int(str(a)[-1])) + 's'
                        o = re.sub(' and','',o)
                        o = re.sub('-',' ',o)
                    else: 
                        o = num2words(int(str(a)[0])) + ' ' + 'hundred' + ' ' + num2words(int(str(a)[-1])) + 'es'
                        o = re.sub(' and','',o)
                        o = re.sub('-',' ',o)
                    return o
                else: 
                    if (str(a)[-1] != '6') :
                        o = num2words(int(str(a)[:1])) + ' ' + num2words(int(str(a)[1:])) + 's'
                        o = re.sub(' and','',o)
                        o = re.sub('-',' ',o)
                        return o
                    elif (str(a)[-2:] == '16'):
                        o = num2words(int(str(a))) + 's'
                        o = re.sub(' and','',o)
                        o = re.sub('-',' ',o)
                        return o
                    else:
                        o = num2words(int(str(a)[:1])) + ' ' + num2words(int(str(a)[1:])) + 'es'
                        o = re.sub(' and','',o)
                        o = re.sub('-',' ',o)
                        return o
            elif (len(str(a)) == 2):
                if (str(a) == '00'):
                    o = 'o o'
                    return o
                elif (str(a)[0] == '0'):
                    if (str(a)[1] != '6'):
                        o = 'o' + ' ' + num2words(int(str(a)[-1])) + 's'
                        o = re.sub(' and','',o)
                        o = re.sub('-',' ',o)
                        return o
                    else: 
                        o = 'o' + ' ' + num2words(int(str(a)[-1])) + 'es'
                        o = re.sub(' and','',o)
                        o = re.sub('-',' ',o)
                        return o
                elif (str(a)[-1] != '6'):
                    o = num2words(int(str(a))) + 's'
                    o = re.sub(' and','',o)
                    o = re.sub('-',' ',o)
                    return o
                elif (str(a)[-2:] == '16'):
                    o = num2words(int(str(a))) + 's'
                    o = re.sub(' and','',o)
                    o = re.sub('-',' ',o)
                    return o
                else: 
                    o = num2words(int(str(a))) + 'es'
                    o = re.sub(' and','',o)
                    o = re.sub('-',' ',o)
                    return o
            elif (len(str(a)) == 1):
                if str(a) != '6':
                    o = num2words(int(str(a))) + 's'
                    o = re.sub(' and','',o)
                    o = re.sub('-',' ',o)
                    return o
                elif (str(a)[-2:] == '16'):
                    o = num2words(int(str(a))) + 's'
                    o = re.sub(' and','',o)
                    o = re.sub('-',' ',o)
                    return o
                else: 
                    o = num2words(int(str(a))) + 'es'
                    o = re.sub(' and','',o)
                    o = re.sub('-',' ',o)
                    return o
    else:       
        return a
    
    

def date(a):
    output=[0] * len(a)
    inputdate=a
    space = ' '
    dash = '-'
    slash = '/'
    dot = '.'
    numbers = '0123456789'
    letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    weekdays_full = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    weekdays = {'sun':'sunday','mon':'monday','tue':'tuesday','wed':'wednesday','thu':'thursday','fri':'friday', 'sat':'saturday'}  
    month_full = ['january', 'february','march','april','may','june','july','august','september','october','november','december']    
    month_sim = {'jan':'january', 'feb':'february','mar':'march','apr':'april','may':'may', 'jun': 'june','jul':'july','aug':'august','sept':'september','sep':'september','oct':'october','nov':'november','dec':'december'}
    month_num = {'01':'january', '02':'february','03':'march','04':'april','05':'may', '06': 'june','07':'july','08':'august','09':'september','1':'january', '2':'february','3':'march','4':'april','5':'may', '6': 'june','7':'july','8':'august','9':'september','10':'october','11':'november','12':'december'}
    for j in range(len(a)):
        try:
        cnt = Counter(inputdate[j])
        cnt_number = sum(cnt[x] for x in numbers)
        cnt_space = sum(cnt[x] for x in space)
        cnt_dash = sum(cnt[x] for x in dash)
        cnt_slash = sum(cnt[x] for x in slash)
        cnt_dot = sum(cnt[x] for x in dot) 
        seg = re.findall(r"[a-zA-Z0-9]+|[a-zA-Z0-9]+|[a-zA-Z0-9]+",str(inputdate[j]))
        inputdatebcad = re.sub('[ \.]','', inputdate[j])
        segforbcad = re.findall(r"[0-9]+|[a-fA-F]+",str(inputdatebcad))
        if len(seg) == 1:
            segfors = re.findall(r"[0-9]+|[s]",str(inputdate[j]))
            if (len(segfors) == 1):
                if (str(segfors[0])[0] in numbers):
                    output[j] = dateyear(seg[0])
            elif (len(segfors) == 2): 
                if (str(segfors[1]) == 's'):
                    if str(segfors[0])[0] in numbers:
                        segfors[0] = re.findall(r"[0-9]+",str(segfors[0]))[0]
                        output[j] = yearpluss(segfors[0])
                        output[j] = re.sub('-',' ',output[j])
        elif len(seg) == 2:
            if str(seg[1]) == 's':
                output[j] = yearpluss(seg[0])
                output[j] = re.sub('-',' ',output[j])  
            elif str(seg[0])[0] in numbers:
                seg[0] = re.findall(r"[0-9]+",str(seg[0]))[0]
                if str(seg[1])[0] in letters:
                    seg[1] = re.findall(r"[a-zA-Z]+",str(seg[1]))[0]
                    seg[1] = seg[1].lower()
                    if seg[1] in month_sim:
                        output[j] = 'the'+ ' ' + num2words(int(str(seg[0])),ordinal = True) + ' ' + 'of' + ' ' + month_sim[seg[1]]
                        output[j] = re.sub('-',' ',output[j])
                    elif str(seg[1]) in ['a','b']:
                        output[j] = dateyear(seg[0])
                        output[j] = re.sub('-',' ',output[j])
                    elif seg[1] not in month_sim:
                        output[j] = 'the'+ ' ' + num2words(int(str(seg[0])),ordinal = True) + ' ' + 'of' + ' ' + str(seg[1]).lower()
                        output[j] = re.sub('-',' ',output[j])
            elif str(seg[0])[0] in letters:
                seg[0] = re.findall(r"[a-zA-Z]+",str(seg[0]))[0]
                seg[0] = seg[0].lower()
                seg[1] = re.findall(r"[0-9]+",str(seg[1]))[0]
                if str(seg[0]) in month_sim:
                    if int(str(seg[1])) <= 31:
                        output[j] = month_sim[str(seg[0])] + ' ' + num2words(int(str(seg[1])),ordinal = True)
                        output[j] = re.sub('-',' ',output[j])
                    else: 
                        output[j] = month_sim[str(seg[0])] + ' ' + dateyear(seg[1])
                        output[j] = re.sub('-',' ',output[j])
                else:
                    if int(str(seg[1])) <= 31:
                        output[j] = str(seg[0]).lower()+ ' ' + num2words(int(str(seg[1])),ordinal = True)
                        output[j] = re.sub('-',' ',output[j])
                    else:
                        output[j] = str(seg[0]).lower()+ ' ' + dateyear(seg[1])
                        output[j] = re.sub('-',' ',output[j])  
        elif len(seg) == 3: 
            if str(seg[0])[0] in letters:
                seg[0] = re.findall(r"[a-zA-Z]+",str(seg[0]))[0]
                seg[0] = seg[0].lower()
                if str(seg[0]) in weekdays:
                    if str(seg[2])[0] in letters:
                        seg[2] = re.findall(r"[a-zA-Z]+",str(seg[2]))[0]
                        seg[2] = seg[2].lower()
                        if str(seg[2]) in month_sim:
                            seg[2] = re.findall(r"[a-zA-Z]+",str(seg[2]))[0]
                            if str(seg[1])[0] in numbers:
                                seg[1] = re.findall(r"[0-9]+",str(seg[1]))[0]
                                output[j] = weekdays[str(seg[0])] + ' the ' + num2words(int(str(seg[1])),ordinal = True) + ' of ' + month_sim[seg[2]]
                                output[j] = re.sub('-',' ',output[j]) 
                        else: 
                            seg[2] = re.findall(r"[a-zA-Z]+",str(seg[2]))[0]
                            if str(seg[1])[0] in numbers:
                                seg[1] = re.findall(r"[0-9]+",str(seg[1]))[0]
                                output[j] = weekdays[str(seg[0])] + ' the ' + num2words(int(str(seg[1])),ordinal = True) + ' of ' + seg[2].lower()
                                output[j] = re.sub('-',' ',output[j]) 
                    elif str(seg[2])[0] in numbers:
                        seg[2] = re.findall(r"[0-9]+",str(seg[2]))[0]
                        if str(seg[1])[0] in letters:
                            seg[1] = re.findall(r"[a-zA-Z]+",str(seg[1]))[0]
                            seg[1] = seg[1].lower()
                            if str(seg[1]) in month_sim:
                                output[j] = weekdays[str(seg[0])] + ' ' + month_sim[str(seg[1])] + ' ' + num2words(int(str(seg[2])), ordinal = True)
                                output[j] = re.sub('-',' ',output[j])
                            else: 
                                output[j] = weekdays[str(seg[0])] + ' ' + str(seg[1]) + ' ' + num2words(int(str(seg[2])), ordinal = True)
                                output[j] = re.sub('-',' ',output[j])
                elif str(seg[0]) in weekdays_full:
                    if str(seg[2])[0] in letters:
                        seg[2] = re.findall(r"[a-zA-Z]+",str(seg[2]))[0]
                        seg[2] = seg[2].lower()
                        if str(seg[2]) in month_sim:
                            seg[2] = re.findall(r"[a-zA-Z]+",str(seg[2]))[0]
                            if str(seg[1])[0] in numbers:
                                seg[1] = re.findall(r"[0-9]+",str(seg[1]))[0]
                                output[j] = str(seg[0]) + ' the ' + num2words(int(str(seg[1])),ordinal = True) + ' of ' + month_sim[seg[2]]
                                output[j] = re.sub('-',' ',output[j]) 
                        else: 
                            seg[2] = re.findall(r"[a-zA-Z]+",str(seg[2]))[0]
                            if str(seg[1])[0] in numbers:
                                seg[1] = re.findall(r"[0-9]+",str(seg[1]))[0]
                                output[j] = str(seg[0]) + ' the ' + num2words(int(str(seg[1])),ordinal = True) + ' of ' + seg[2].lower()
                                output[j] = re.sub('-',' ',output[j])
                    elif str(seg[2])[0] in numbers:
                        seg[2] = re.findall(r"[0-9]+",str(seg[2]))[0]
                        if str(seg[1])[0] in letters:
                            seg[1] = re.findall(r"[a-zA-Z]+",str(seg[1]))[0]
                            seg[1] = seg[1].lower()
                            if str(seg[1]) in month_sim:
                                output[j] = str(seg[0]) + ' ' + month_sim[str(seg[1])] + ' ' + num2words(int(str(seg[2])), ordinal = True)
                                output[j] = re.sub('-',' ',output[j])
                            else: 
                                output[j] = str(seg[0]) + ' ' + str(seg[1]) + ' ' + num2words(int(str(seg[2])), ordinal = True)
                                output[j] = re.sub('-',' ',output[j])                     
                elif str(seg[1])[0] in letters:
                    seg[2] = re.findall(r"[0-9]+",str(seg[2]))[0]
                    output[j] = str(seg[0]).lower()+ ' ' + str(seg[1]).lower() + ' ' + num2words(int(str(seg[2])),ordinal = True)
                    output[j] = re.sub('-',' ',output[j])
                elif str(seg[1])[0] in numbers:
                    seg[1] = re.findall(r"[0-9]+",str(seg[1]))[0]
                    if str(seg[0]) in month_sim:
                        if str(seg[2])[0] == '0':                            
                            output[j] = month_sim[str(seg[0])]+ ' ' + num2words(int(str(seg[1])),ordinal = True) + ' o ' + dateyear(seg[2][-1])
                            output[j] = re.sub('-',' ',output[j])
                        else:
                            output[j] = month_sim[str(seg[0])]+ ' ' + num2words(int(str(seg[1])),ordinal = True) + ' ' + dateyear(seg[2])
                            output[j] = re.sub('-',' ',output[j])
                    elif str(seg[2])[0] in letters:
                        seg[2] = re.findall(r"[a-zA-Z]+",str(seg[2]))[0]
                        seg[2] = seg[2].lower()
                        if str(seg[2]) in month_sim:
                            output[j] = 'the' + ' ' + seg[0] + ' ' + num2words(int(str(seg[1])), ordinal = True) + ' ' + 'of' + ' ' + month_sim[str(seg[2])]
                            output[j] = re.sub('-',' ',output[j])
                        else: 
                            output[j] = 'the' + ' ' + seg[0] + ' ' + num2words(int(str(seg[1])), ordinal = True) + ' ' + 'of' + ' ' + str(seg[2])
                            output[j] = re.sub('-',' ',output[j])
                    else:
                        if str(seg[2])[0] == '0': 
                            output[j] = str(seg[0]).lower() + ' ' + num2words(int(str(seg[1])),ordinal = True) + ' o ' + dateyear(seg[2][-1])
                            output[j] = re.sub('-',' ',output[j])
                        else: 
                            output[j] = str(seg[0]).lower()+ ' ' + num2words(int(str(seg[1])),ordinal = True) + ' ' + dateyear(seg[2])
                            output[j] = re.sub('-',' ',output[j])
            elif str(seg[0])[0] in numbers:
                seg[0] = re.findall(r"[0-9]+",str(seg[0]))[0]
                if str(seg[1])[0] in letters:
                    seg[1] = re.findall(r"[a-zA-Z]+",str(seg[1]))[0]
                    seg[1] = seg[1].lower()
                    seg[0] = re.findall(r"[0-9]+",str(seg[0]))[0]
                    if str(seg[1]) in month_sim:
                        if (int(str(seg[0])) <= 31):
                            output[j] = 'the' + ' ' + num2words(int(str(seg[0])),ordinal = True) + ' ' + 'of' + ' ' + month_sim[str(seg[1])]+ ' ' + dateyear(seg[2])
                            output[j] = re.sub('-',' ',output[j])
                        else: 
                            output[j] = 'the' + ' ' + num2words(int(str(seg[2])),ordinal = True) + ' ' + 'of' + ' ' + month_sim[str(seg[1])]+ ' ' + dateyear(seg[0])
                            output[j] = re.sub('-',' ',output[j])
                    else:
                        if str(seg[2])[0] in numbers:
                            seg[2] = re.findall(r"[0-9]+",str(seg[2]))[0]
                            if (int(seg[2]) <= 100):
                                if str(seg[2])[0] == '0':
                                    output[j] = 'the' + ' ' + num2words(int(str(seg[0])), ordinal = True) + ' ' + 'of' + ' ' + str(seg[1]).lower() + ' ' + ' '.join(str(seg[2]))
                                    output[j] = re.sub('0','o',output[j])
                                    output[j] = re.sub('1','one',output[j])
                                    output[j] = re.sub('2','two',output[j])
                                    output[j] = re.sub('3','three',output[j])
                                    output[j] = re.sub('4','four',output[j])
                                    output[j] = re.sub('5','five',output[j])
                                    output[j] = re.sub('6','six',output[j])
                                    output[j] = re.sub('7','seven',output[j])
                                    output[j] = re.sub('8','eight',output[j])
                                    output[j] = re.sub('9','nine',output[j])
                                    output[j] = re.sub('-',' ',output[j])
                                else:
                                    output[j] = 'the' + ' ' + num2words(int(str(seg[0])),ordinal = True) + ' ' + 'of' + ' ' + str(seg[1]).lower()+ ' ' + dateyear(seg[2])
                                    output[j] = re.sub('-',' ',output[j])
                            else:
                                output[j] = 'the' + ' ' + num2words(int(str(seg[0])),ordinal = True) + ' ' + 'of' + ' ' + str(seg[1]).lower()+ ' ' + dateyear(seg[2])
                                output[j] = re.sub('-',' ',output[j])
                elif str(seg[1])[0] in numbers:
                    if seg[0] in month_num:
                        if seg[1] in month_num:
                            if (int(seg[2]) <= 100):
                                if str(seg[2])[0] == '0':  
                                    output[j] = 'the' + ' ' + num2words(int(str(seg[1])), ordinal = True) + ' ' + 'of' + ' ' + month_num[str(seg[0])] + ' ' + ' '.join(str(seg[2]))
                                    output[j] = re.sub('0','o',output[j])
                                    output[j] = re.sub('1','one',output[j])
                                    output[j] = re.sub('2','two',output[j])
                                    output[j] = re.sub('3','three',output[j])
                                    output[j] = re.sub('4','four',output[j])
                                    output[j] = re.sub('5','five',output[j])
                                    output[j] = re.sub('6','six',output[j])
                                    output[j] = re.sub('7','seven',output[j])
                                    output[j] = re.sub('8','eight',output[j])
                                    output[j] = re.sub('9','nine',output[j])
                                    output[j] = re.sub('-',' ',output[j])
                                else:
                                    output[j] = 'the' + ' ' + num2words(int(str(seg[1])), ordinal = True) + ' ' + 'of' + ' ' + month_num[str(seg[0])] + ' ' + num2words(int(str(seg[2])))
                                    output[j] = re.sub('-',' ',output[j]) 
                            else: 
                                output[j] = 'the' + ' ' + num2words(int(str(seg[1])), ordinal = True) + ' ' + 'of' + ' ' + month_num[str(seg[0])] + ' ' + dateyear(str(seg[2]))
                                output[j] = re.sub('-',' ',output[j]) 
                        else:
                            if (int(seg[2]) <= 100):
                                if str(seg[2])[0] == '0': 
                                    output[j] = month_num[str(seg[0])] + ' ' + num2words(int(str(seg[1])), ordinal = True) + ' ' + ' '.join(str(seg[2]))
                                    output[j] = re.sub('0','o',output[j])
                                    output[j] = re.sub('1','one',output[j])
                                    output[j] = re.sub('2','two',output[j])
                                    output[j] = re.sub('3','three',output[j])
                                    output[j] = re.sub('4','four',output[j])
                                    output[j] = re.sub('5','five',output[j])
                                    output[j] = re.sub('6','six',output[j])
                                    output[j] = re.sub('7','seven',output[j])
                                    output[j] = re.sub('8','eight',output[j])
                                    output[j] = re.sub('9','nine',output[j])
                                    output[j] = re.sub('-',' ',output[j])
                                else:
                                    output[j] = month_num[str(seg[0])] + ' ' + num2words(int(str(seg[1])), ordinal = True) + ' ' + num2words(int(str(seg[2])))
                                    output[j] = re.sub('-',' ',output[j])
                            else:
                                output[j] = month_num[str(seg[0])] + ' ' + num2words(int(str(seg[1])), ordinal = True) + ' ' + dateyear(str(seg[2]))
                                output[j] = re.sub('-',' ',output[j])
                    elif seg[0] not in month_num:
                        if (int(seg[0]) <= 31):
                            if seg[1] in month_num: # For sure it has to be in month_num
                                if seg[2] in month_num:
                                    output[j] = 'the' + ' ' + num2words(int(seg[2]), ordinal = True) + ' ' + 'of' + ' ' + month_num[seg[1]] + ' ' + dateyear(seg[0])
                                    output[j] = re.sub('-',' ',output[j])
                                else:
                                    output[j] = 'the' + ' ' + num2words(int(seg[0]), ordinal = True) + ' ' + 'of' + ' ' + month_num[seg[1]] + ' ' + dateyear(seg[2])
                                    output[j] = re.sub('-',' ',output[j])
                        else:
                            if seg[1] in month_num:
                                if str(seg[2])[0] in numbers:
                                    seg[2] = re.findall(r"[0-9]+",str(seg[2]))[0]# For sure it has to be in month_num
                                    output[j] = 'the' + ' ' + num2words(int(str(seg[2])), ordinal = True) + ' ' + 'of' + ' ' + month_num[seg[1]] + ' ' + dateyear(seg[0])
                                    output[j] = re.sub('-',' ',output[j])
                                    
        elif len(seg) == 4:
            if str(seg[0])[0] in letters:
                seg[0] = re.findall(r"[a-zA-Z]+",str(seg[0]))[0]
                seg[0] = seg[0].lower()
                if str(seg[0]) in weekdays:
                    if str(seg[1])[0] in letters:
                        seg[1] = re.findall(r"[a-zA-Z]+",str(seg[1]))[0]
                        seg[1] = seg[1].lower()
                        if str(seg[1]) in month_sim:
                            seg[2] = re.findall(r"[0-9]+",str(seg[2]))[0]
                            output[j] = weekdays[str(seg[0])] + ' ' + month_sim[str(seg[1])] + ' ' + num2words(int(str(seg[2])),ordinal = True) + ' ' + dateyear(seg[3])
                            output[j] = re.sub('-',' ',output[j]) 
                        else: 
                            seg[2] = re.findall(r"[0-9]+",str(seg[2]))[0]
                            output[j] = weekdays[str(seg[0])] + ' ' + str(seg[1]) + ' ' + num2words(int(str(seg[2])),ordinal = True) + ' ' + dateyear(seg[3])
                            output[j] = re.sub('-',' ',output[j]) 
                    else:
                        if str(seg[1])[0] in numbers:
                            seg[1] = re.findall(r"[0-9]+",str(seg[1]))[0]
                            if str(seg[2])[0] in letters:
                                seg[2] = re.findall(r"[a-zA-Z]+",str(seg[2]))[0]
                                seg[2] = seg[2].lower()
                                if str(seg[2]) in month_sim:
                                    output[j] = weekdays[str(seg[0])] + ' ' + 'the' + ' ' + num2words(int(str(seg[1])),ordinal = True) + ' ' + 'of' + ' ' + month_sim[str(seg[2])] + ' ' + dateyear(seg[3])
                                    output[j] = re.sub('-',' ',output[j]) 
                                else: 
                                    output[j] = weekdays[str(seg[0])] + ' ' + 'the' + ' ' + num2words(int(str(seg[1])),ordinal = True) + ' ' + 'of' + ' ' + str(seg[2]).lower() + ' ' + dateyear(seg[3])
                                    output[j] = re.sub('-',' ',output[j]) 
                            elif str(seg[2])[0] in numbers:
                                seg[2] = re.findall(r"[0-9]+",str(seg[2]))[0]
                                if seg[2] in month_num:
                                    if str(seg[3])[0] in numbers:
                                        seg[3] = re.findall(r"[0-9]+",str(seg[3]))[0]
                                        output[j] = weekdays[str(seg[0])] + ' ' + 'the' + ' ' + num2words(int(str(seg[3])),ordinal = True) + ' ' + 'of' + ' ' + month_num[str(seg[2])] + ' ' + dateyear(seg[1])
                                        output[j] = re.sub('-',' ',output[j])
                else:
                    if str(seg[0]) in weekdays_full:
                        if str(seg[1])[0] in letters:
                            seg[1] = re.findall(r"[a-zA-Z]+",str(seg[1]))[0]
                            seg[1] = seg[1].lower()
                            seg[2] = re.findall(r"[0-9]+",str(seg[2]))[0]
                            if str(seg[1]) in month_sim:
                                output[j] = str(seg[0]).lower() + ' ' + month_sim[str(seg[1])] + ' ' + num2words(int(str(seg[2])),ordinal = True) + ' ' + dateyear(seg[3])
                                output[j] = re.sub('-',' ',output[j]) 
                            else: 
                                output[j] = str(seg[0]).lower() + ' ' + str(seg[1]) + ' ' + num2words(int(str(seg[2])),ordinal = True) + ' ' + dateyear(seg[3])
                                output[j] = re.sub('-',' ',output[j]) 
                        elif str(seg[1])[0] in numbers:
                            seg[1] = re.findall(r"[0-9]+",str(seg[1]))[0]
                            if str(seg[2])[0] in letters:
                                seg[2] = re.findall(r"[a-zA-Z]+",str(seg[2]))[0]
                                if str(seg[2]) in month_sim:
                                    output[j] = str(seg[0]).lower() + ' ' + 'the' + ' ' + num2words(int(str(seg[1])),ordinal = True) + ' ' + 'of' + ' ' + month_sim[str(seg[2])] + ' ' + dateyear(seg[3])
                                    output[j] = re.sub('-',' ',output[j]) 
                                else: 
                                    output[j] = str(seg[0]).lower() + ' ' + 'the' + ' ' + num2words(int(str(seg[1])),ordinal = True) + ' ' + 'of' + ' ' + str(seg[2]).lower() + ' ' + dateyear(seg[3])
                                    output[j] = re.sub('-',' ',output[j]) 
                            elif str(seg[2])[0] in numbers:
                                seg[2] = re.findall(r"[0-9]+",str(seg[2]))[0]
                                if str(seg[1]) in month_num:
                                    if str(seg[3])[0] in numbers:
                                        seg[3] = re.findall(r"[0-9]+",str(seg[3]))[0]
                                        if (int(str(seg[3])) <= 100):
                                            if str(seg[3])[0] == '0':
                                                output[j] = str(seg[0]) + ' ' + month_num[str(seg[1])] + ' ' + num2words(int(str(seg[2])), ordinal = True) + ' ' + ' '.join(str(seg[3]))
                                                output[j] = re.sub('0','o',output[j])
                                                output[j] = re.sub('1','one',output[j])
                                                output[j] = re.sub('2','two',output[j])
                                                output[j] = re.sub('3','three',output[j])
                                                output[j] = re.sub('4','four',output[j])
                                                output[j] = re.sub('5','five',output[j])
                                                output[j] = re.sub('6','six',output[j])
                                                output[j] = re.sub('7','seven',output[j])
                                                output[j] = re.sub('8','eight',output[j])
                                                output[j] = re.sub('9','nine',output[j])
                                                output[j] = re.sub('-',' ',output[j])
                                            else: 
                                                output[j] = str(seg[0]) + ' ' + month_num[str(seg[1])] + ' ' + num2words(int(str(seg[2])), ordinal = True) + ' ' + dateyear(str(seg[3]))
                                                output[j] = re.sub('-',' ',output[j])
                                        else: 
                                            output[j] = str(seg[0]) + ' ' + month_num[str(seg[1])] + ' ' + num2words(int(str(seg[2])), ordinal = True) + ' ' + dateyear(str(seg[3]))
                                            output[j] = re.sub('-',' ',output[j])
                                elif (int(str(seg[1])) <= 31):
                                    if str(seg[3])[0] in numbers:
                                        seg[3] = re.findall(r"[0-9]+",str(seg[3]))[0]
                                        if (int(str(seg[3])) <= 100):
                                            if str(seg[3])[0] == '0':
                                                output[j] = str(seg[0]) + ' ' + 'the' + ' ' + num2words(int(str(seg[1])), ordinal = True) + ' ' + 'of' + ' ' + month_num[str(seg[2])] + ' ' + ' '.join(str(seg[3]))
                                                output[j] = re.sub('0','o',output[j])
                                                output[j] = re.sub('1','one',output[j])
                                                output[j] = re.sub('2','two',output[j])
                                                output[j] = re.sub('3','three',output[j])
                                                output[j] = re.sub('4','four',output[j])
                                                output[j] = re.sub('5','five',output[j])
                                                output[j] = re.sub('6','six',output[j])
                                                output[j] = re.sub('7','seven',output[j])
                                                output[j] = re.sub('8','eight',output[j])
                                                output[j] = re.sub('9','nine',output[j])
                                                output[j] = re.sub('-',' ',output[j])
                                            else: 
                                                output[j] = str(seg[0]) + ' ' + 'the' + ' ' + num2words(int(str(seg[1])), ordinal = True) + ' ' + 'of' + ' ' + month_num[str(seg[2])] + ' ' + dateyear(str(seg[3]))
                                                output[j] = re.sub('-',' ',output[j])
                                        else: 
                                            output[j] = str(seg[0]) + ' ' + 'the' + ' ' + num2words(int(str(seg[1])), ordinal = True) + ' ' + 'of' + ' ' + month_num[str(seg[2])] + ' ' + dateyear(str(seg[3]))
                                            output[j] = re.sub('-',' ',output[j])
                    else: 
                        if str(seg[1])[0] in letters:
                            seg[1] = re.findall(r"[a-zA-Z]+",str(seg[1]))[0]
                            seg[1] = seg[1].lower()
                            seg[2] = re.findall(r"[0-9]+",str(seg[2]))[0]
                            if str(seg[1]) in month_sim:
                                output[j] = str(seg[0]).lower() + ' ' + month_sim[str(seg[1])] + ' ' + num2words(int(str(seg[2])),ordinal = True) + ' ' + dateyear(seg[3])
                                output[j] = re.sub('-',' ',output[j]) 
                            else: 
                                output[j] = str(seg[0]).lower() + ' ' + str(seg[1]) + ' ' + num2words(int(str(seg[2])),ordinal = True) + ' ' + dateyear(seg[3])
                                output[j] = re.sub('-',' ',output[j]) 
                        else:
                            seg[1] = re.findall(r"[0-9]+",str(seg[1]))[0]
                        # seg[2] = re.findall(r"[a-zA-Z]+",str(seg[2]))[0]
                            if str(seg[2]) in month_sim:
                                output[j] = str(seg[0]).lower() + ' ' + 'the' + ' ' + num2words(int(str(seg[1])),ordinal = True) + ' ' + 'of' + ' ' + month_sim[str(seg[2])] + ' ' + dateyear(seg[3])
                                output[j] = re.sub('-',' ',output[j]) 
                            else: 
                                output[j] = str(seg[0]).lower() + ' ' + 'the' + ' ' + num2words(int(str(seg[1])),ordinal = True) + ' ' + 'of' + ' ' + str(seg[2]).lower() + ' ' + dateyear(seg[3])
                                output[j] = re.sub('-',' ',output[j])        
        if len(segforbcad) >= 2:
            if len(segforbcad) == 2:
                if str(segforbcad[1])[0] in letters:
                    segforbcad[1] = re.sub('[\.]', '' ,str(segforbcad[1]))
                    segforbcad[1] = segforbcad[1].lower()
                    if str(segforbcad[1]) in ['bc','ad','ce','bce','af','nc']:
                        if len(segforbcad[0]) == 1:
                            output[j] = 'o' + ' ' + dateyear(segforbcad[0]) + ' ' + ' '.join(str(segforbcad[1]))
                            output[j] = re.sub('-',' ',output[j])
                        else:
                            output[j] = dateyear(segforbcad[0]) + ' ' + ' '.join(str(segforbcad[1]))
                            output[j] = re.sub('-',' ',output[j]) 
            else:
                if str(segforbcad[-1])[0] in letters:
                    segforbcad[-1] = re.sub('[\.]', '' ,str(segforbcad[-1]))
                    segforbcad[-1] = segforbcad[-1].lower()
                    if str(segforbcad[-1]) in ['bc','ad','ce','bce','af','nc']:
                        if len(seg) == 4:
                            if str(seg[1])[0] in letters:
                                seg[1] = re.findall(r"[a-zA-Z]+",str(seg[1]))[0]
                                seg[1] = seg[1].lower()
                                if str(seg[1]) in month_full:
                                    output[j] = 'the' + ' ' + num2words(int(str(seg[0])), ordinal = True) + ' ' + 'of' + ' ' + str(seg[1]) + ' ' + dateyear(seg[2]) + ' ' + ' '.join(str(segforbcad[-1])) 
                                    output[j] = re.sub('-',' ',output[j]) 
                        elif len(seg) == 3:
                            if str(seg[1])[0] in letters:
                                seg[1] = re.findall(r"[a-zA-Z]+",str(seg[1]))[0]
                                seg[1] = seg[1].lower()
                                if str(seg[1]) in month_full:
                                    output[j] = 'the' + ' ' + num2words(int(str(seg[0])), ordinal = True) + ' ' + 'of' + ' ' + str(seg[1]) + ' ' + ' '.join(str(segforbcad[-1])) 
                                    output[j] = re.sub('-',' ',output[j])                
        if (str(output[j])[:7] == 'the the'):
            output[j] = output[j][4:]
    return output  

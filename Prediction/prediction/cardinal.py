from num2words import num2words
from collections import Counter
import numpy as np
import pandas as pd
import re

numerals = [
        {'letter': 'M', 'value': 1000},
        {'letter': 'D', 'value': 500},
        {'letter': 'C', 'value': 100},
        {'letter': 'L', 'value': 50},
        {'letter': 'X', 'value': 10},
        {'letter': 'V', 'value': 5},
        {'letter': 'I', 'value': 1},
    ]
def isinteger(a):
    try:
        int(a)
        return True
    except ValueError:
        return False

def roman_to_arabic(number):
    index_by_letter = {}
    for index in (range(len(numerals))):
        index_by_letter[numerals[index]['letter']] = index

    result = 0
    previous_value = None
    for letter in reversed(number):
        index = index_by_letter[letter]
        value = numerals[index]['value']
        if (previous_value is None) or (previous_value <= value):
            result += value
        else:
            result -= value
        previous_value = value
    return result

def cardinal(a):
    output=[0] * len(a)
    romans='MDCLXVI'
    numbers='-0123456789'
    purenumbers='0123456789'
    dot = '.'
    space = ' '
    for j in range(len(a)):
        try:
            cnt = Counter(str(a[j]))
            cnt_space = sum(cnt[x] for x in space)
            cnt_dot = sum(cnt[x] for x in dot)
            seg = re.findall(r"[\-0-9,]+|[MDCLXVI]+|[a-z]+",str(a[j]))
            if len(seg) == 1:
                if seg[0][0] in numbers:
                    seg[0] = re.sub('\,','',str(seg[0]))
                    if str(seg[0][-1]) not in purenumbers:
                        seg[0] = str(seg[0])[:-1]
                        output[j] = num2words(int(str(seg[0])))
                        output[j] = re.sub('[,/]','',output[j])
                        output[j] = re.sub(' and ',' ',output[j])
                        output[j] = re.sub('-',' ',output[j])
                    else:
                        output[j] = num2words(int(str(seg[0])))
                        output[j] = re.sub('[,/]','',output[j])
                        output[j] = re.sub(' and ',' ',output[j])
                        output[j] = re.sub('-',' ',output[j])
                elif seg[0][0] in romans:
                    output[j] = str(num2words(int(roman_to_arabic(seg[0]))))
                    output[j] = re.sub('[,/]','',output[j])
                    output[j] = re.sub(' and ',' ',output[j])
                    output[j] = re.sub('-',' ',output[j])
            elif len(seg) == 2:
                if seg[0][0] in numbers:
                    if cnt_space >= 1:
                        a[j] = re.sub('[ a-zA-Z]','',str(a[j]))
                        output[j] = num2words(int(str(a[j])))
                        output[j] = re.sub('[,/]','',output[j])
                        output[j] = re.sub(' and ',' ',output[j])
                        output[j] = re.sub('-',' ',output[j])
                    else:
                        seg[0] = re.sub('\,','',str(seg[0]))
                        output[j] = num2words(int(str(seg[0]))) + '\'s'
                        output[j] = re.sub('[,/]','',output[j])
                        output[j] = re.sub(' and ',' ',output[j])
                        output[j] = re.sub('-',' ',output[j])
                elif seg[0][0] in romans:
                    output[j] = str(num2words(int(roman_to_arabic(seg[0])))) + '\'s'
                    output[j] = re.sub('[,/]','',output[j])
                    output[j] = re.sub(' and ',' ',output[j])
                    output[j] = re.sub('-',' ',output[j])
                elif cnt_dot >= 1:
                    output[j] = decimal(a[j])
            elif len(seg) >= 3:
                if cnt_space >= 2:
                        a[j] = re.sub(' ','',str(a[j]))
                        output[j] = num2words(int(str(a[j])))
                        output[j] = re.sub('[,/]','',output[j])
                        output[j] = re.sub(' and ',' ',output[j])
                        output[j] = re.sub('-',' ',output[j])
                else:
                    a[j] = re.sub('[, a-zA-Z]','',str(a[j]))
                    output[j] = num2words(int(str(a[j])))
                    output[j] = re.sub('[,/]','',output[j])
                    output[j] = re.sub(' and ',' ',output[j])
                    output[j] = re.sub('-',' ',output[j]) 
        except TypeError:
            output[j]='AAAis is wrong!'
        except ValueError:
            output[j]='AAAis is wrong!'
    return output
